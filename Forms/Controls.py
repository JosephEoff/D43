from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QWidget,  QApplication,  QFileDialog
import os
from quantiphy import Quantity
import cv2
import csv
from Forms.Ui_Controls import Ui_Controls

class Controls(QWidget, Ui_Controls):
    def __init__(self, parent):
        super(QWidget, self).__init__()
                
        self.transparentThreshold = 20
        self.timer =  None
        self.thresholdMode = cv2.THRESH_BINARY
        self.fps = 24
        self.videocapture = None 
        self.setupUi(self)
        self.dockWidgetCalibration.hide()
        self.toolButtonCalibrate.clicked.connect(self.doShowCalibration)
        
        self.availableCameras = self.getListOfCameras()
        self.comboBoxCameraSelect.addItems(self.availableCameras)
        self.checkBoxPause.stateChanged.connect(self.doPauseStateChanged)
        self.checkBoxLines.stateChanged.connect(self.doLineModeSelect)
        self.pushButtonCrop.clicked.connect(self.on_buttonCropClicked)
        self.pushButtonReset.clicked.connect(self.on_buttonResetClicked)
        self.pushButtonGrid.clicked.connect(self.on_buttonGridClicked)
        self.pushButtonSnapshot .clicked.connect(self.on_buttonSnapshotClicked)
        self.pushButtonDigitizedData.clicked.connect(self.on_SaveDigitizedDataClicked)
        self.widgetCursorControl.cursorMoved.connect(self.updateOnCursorMove)

        
        self.timebase = [  ("5 Secs", 5.0),  ("2 Secs", 2.0),   ("1Sec", 1.0),  
                                    ("500 ms", 0.5),  ("200 ms", 0.2),  ("100 ms", 0.1), 
                                    ("50 ms", 0.05),  ("20 ms", 0.02),  ("10 ms", 0.01),  
                                    ("5 ms", 0.005),  ("2 ms",  0.002), ("1 ms",  0.001), 
                                    ("500 us", 0.0005),  ("200 us", 0.0002),  ("100 us", 0.0001), 
                                    ("50 us", 0.00005),  ("20 us", 0.00002),  ("10 us", 0.00001), 
                                    ("5 us", 0.000005),  ("2 us", 0.000002),  ("1 us",  0.000001), 
                                     ("0.5 us", 0.0000005)]
                                     
        self.voltages = [ ("50 V", 50.0),  ("20 V", 20.0),  ("10 V", 10.0), 
                                  ("5 V", 5.0),  ("2 V", 2.0),  ("1 V", 1.0), 
                                  ("500 mV", 0.5),  ("200 mV", 0.2),  ("100 mV", 0.1)]
                                  
        self.multipliers = [("1", 1.0),  ("10", 0.1),  ("100", 0.01),  ("1000", 0.001)]

        self.settings = QSettings()
        self.rawImageWidth = int(self.settings.value("rawImageWidth",  640))
        self.rawImageHeight = int(self.settings.value("rawImageHeight",  480))
        self.crop_X1 = int(self.settings.value("crop_X1",  0))
        self.crop_X2 = int(self.settings.value("crop_X2",  640))
        self.crop_Y1 = int(self.settings.value("crop_Y1",  0))
        self.crop_Y2 = int(self.settings.value("crop_Y2",  480))
        self.grid_X1 = int(self.settings.value("grid_X1",  0))
        self.grid_X2 = int(self.settings.value("grid_X2",  640))
        self.grid_Y1 = int(self.settings.value("grid_Y1",  0))
        self.grid_Y2 = int(self.settings.value("grid_Y2",  480))
        self.grid_HorizontalDivisions = int(self.settings.value("grid_HorizontalDivisions",  8))
        self.grid_VerticalDivisions = int(self.settings.value("grid_VerticalDivisions",  6))
        self.spinBoxHorizontalDivisions.setValue(self.grid_HorizontalDivisions)
        self.spinBoxVerticalDivisions.setValue(self.grid_VerticalDivisions)
        self.updateGrid()        
        self.updateDigitizingRange()        
        self.fillComboBoxes(self.settings)
        self.setComboBoxSelectedItemFromSettings(self.settings, "Camera", self.comboBoxCameraSelect )
        self.setComboBoxSelectedItemFromSettings(self.settings, "Multiplier_Selected",  self.comboBoxMultiplier)
        self.setComboBoxSelectedItemFromSettings(self.settings, "Timebase_Selected",  self.comboBoxTimeBase)
        self.setComboBoxSelectedItemFromSettings(self.settings, "VerticalDeflection_Selected",  self.comboBoxVerticalDeflection)
        self.comboBoxMultiplier.currentIndexChanged.connect(self.settingChanged)
        self.comboBoxTimeBase.currentIndexChanged.connect(self.settingChanged)
        self.comboBoxVerticalDeflection.currentIndexChanged.connect(self.settingChanged)
        self.comboBoxCameraSelect.currentIndexChanged.connect(self.changeCamera)
        self.start()
        self.updateOnCursorMove()
    
    def on_SaveDigitizedDataClicked(self):
        data = self.widgetDigitizedView.getDigitizedData()
        data = self.widgetCursorControl.getZero_pixels() - data
        data = data * self.getVoltsPerPixel()
        filename,  filter = QFileDialog.getSaveFileName(self, 'Save CSV Data File',  '',  'CSV Files (*.csv)')
        if filename:
            filename, extension = os.path.splitext(filename)
            filename = filename + '.csv'
            timePerPixel = self.getSecondsPerPixel()
            count = 0
            x1, x2 = self.widgetDigitizedView.getRange()
            with open( filename, 'w') as csvfile:
                 for x in range(x1, x2+1):
                    csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csvwriter.writerow([count * timePerPixel,   data[x]])
                    count = count + 1
    
    def on_buttonSnapshotClicked(self):
        snapshot = QApplication.primaryScreen().grabWindow(self.groupBoxDisplay.winId())
        filename,  filter = QFileDialog.getSaveFileName(self, 'Save Snapshot',  '',  'PNG Files (*.png)')
        if filename:
            filename, extension = os.path.splitext(filename)
            filename = filename + '.png'
            snapshot.save(filename,  "PNG")        
    
    def doShowCalibration(self):
        self.dockWidgetCalibration.setFloating(True)
        self.dockWidgetCalibration.show()
        
    def fillComboBoxes(self,  settings):
        # This looks stupidly complicated.  If I just let QT take care of things, it would be much shorter.
        # I want user editable entries for these values in the settings file, though.
        # Qt encodes the strings and values in a way that you can't easily edit with a text editor.
        # Hence extra conversion steps.
        # For example, the multipliers entry looks like this:
        # multipliers="('1', 1.0), ('10', 0.1), ('100', 0.01), ('1000', 0.001)"
        # Easy enough to edit
        if not settings.contains("timebase"):
            settings.setValue("timebase",  str(self.timebase).strip('[]'))
        self.timebase = self.listOfTuplesFromString(settings.value("timebase"))
        self.fillComboBoxFromListOfTuples(self.comboBoxTimeBase,  self.timebase)
        
        if not settings.contains("voltages"):
            settings.setValue("voltages",  str(self.voltages).strip('[]'))
        self.voltages = self.listOfTuplesFromString(settings.value("voltages"))
        self.fillComboBoxFromListOfTuples(self.comboBoxVerticalDeflection,  self.voltages)
    
        if not settings.contains("multipliers"):
            settings.setValue("multipliers",  str(self.multipliers).strip('[]'))
        self.multipliers = self.listOfTuplesFromString(settings.value("multipliers"))
        self.fillComboBoxFromListOfTuples(self.comboBoxMultiplier,  self.multipliers)
        
    def setComboBoxSelectedItemFromSettings(self,  settings,  settingName,  combobox):
        savedItemName = settings.value(settingName,  "-")
        itemIndex =  combobox.findText(savedItemName )
        if itemIndex>=0:
            combobox.setCurrentIndex(itemIndex)
        
    def fillComboBoxFromListOfTuples(self, combobox,   valuesList):
        combobox.clear()
        for item in  valuesList:
            combobox.addItem(item[0],  item[1])

    def listOfTuplesFromString(self, formattedString):
        return eval("[%s]" % formattedString)
        
    def updateGrid(self):
        self.widgetGridView.updateGridSpacing(self.grid_X1,  self.grid_X2,  self.grid_Y1,  self.grid_Y2,  self.grid_HorizontalDivisions,  self.grid_VerticalDivisions)

    def updateDigitizingRange(self):
        self.widgetDigitizedView.setDigitizingRange(self.grid_X1,  self.grid_X2)
        
    def on_buttonCropClicked(self):
        self.crop_X1 = self.widgetCursorControl.getX1_pixels()
        self.crop_X2 = self.widgetCursorControl.getX2_pixels()
        self.crop_Y1 = self.widgetCursorControl.getY1_pixels()
        self.crop_Y2 = self.widgetCursorControl.getY2_pixels()
        
        if self.crop_X2<self.crop_X1:
            self.crop_X1,  self.crop_X2 = self.crop_X2,  self.crop_X1
        
        if self.crop_Y2<self.crop_Y1:
            self.crop_Y1,  self.crop_Y2 = self.crop_Y2,  self.crop_Y1
            
        self.settings.setValue("crop_X1",  self.crop_X1)
        self.settings.setValue("crop_X2",  self.crop_X2)
        self.settings.setValue("crop_Y1",  self.crop_Y1)
        self.settings.setValue("crop_Y2",  self.crop_Y2)
        
    def on_buttonGridClicked(self):
        self.grid_X1 = self.widgetCursorControl.getX1_pixels()
        self.grid_X2 = self.widgetCursorControl.getX2_pixels()
        self.grid_Y1 = self.widgetCursorControl.getY1_pixels()
        self.grid_Y2 = self.widgetCursorControl.getY2_pixels()
        self.grid_HorizontalDivisions = self.spinBoxHorizontalDivisions.value()
        self.grid_VerticalDivisions = self.spinBoxVerticalDivisions.value()
        
        if self.grid_X2<self.grid_X1:
            self.grid_X1,  self.grid_X2 = self.grid_X2,  self.grid_X1
        
        if self.grid_Y2<self.grid_Y1:
            self.grid_Y1,  self.grid_Y2 = self.grid_Y2,  self.grid_Y1
        
        self.updateGrid()
        self.updateDigitizingRange()
        
        self.settings.setValue("grid_X1",  self.grid_X1)
        self.settings.setValue("grid_X2",  self.grid_X2)
        self.settings.setValue("grid_Y1", self.grid_Y1)
        self.settings.setValue("grid_Y2",  self.grid_Y2)
        self.settings.setValue("grid_HorizontalDivisions",  self.grid_HorizontalDivisions)
        self.settings.setValue("grid_VerticalDivisions",  self.grid_VerticalDivisions)
    
    def on_buttonResetClicked(self):
        self.crop_X1 = 0
        self.crop_X2 = self.rawImageWidth
        self.crop_Y1 = 0
        self.crop_Y2 = self.rawImageHeight
    
    def doPauseStateChanged(self, state):
        if state ==QtCore.Qt.Checked:
            self.stop()
        else:
            self.start()
    
    def doLineModeSelect(self,  state):
        if state ==QtCore.Qt.Checked:
            self.widgetDigitizedView.setLineMode(True)
        else:
            self.widgetDigitizedView.setLineMode(False)
    
    def changeCamera(self, selectedCameraIndex):
        self.settings.setValue("Camera",  self.comboBoxCameraSelect.currentText())
        self.stop()
        self.start()
    
    def start(self):
        cameraindex = self.comboBoxCameraSelect.currentIndex()
        self.videocapture = cv2.VideoCapture(cameraindex )
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./self.fps)

    def stop(self):
        if not self.timer is None:
            self.timer.stop()
        if not self.videocapture is None:
            self.videocapture.release()
        
    def getListOfCameras(self):
        camerasInfoList = QtMultimedia.QCameraInfo.availableCameras()
        camerasList=[]
        for cameraInfo in camerasInfoList:
            camerasList.append(cameraInfo.description())
        return camerasList
    
    def nextFrameSlot(self):
        try:
            ret, frame = self.videocapture.read()
            if not ret:
                self.stop()
                self.start()
                return
        # Assume Webcam gives BGR format images
        # May need to add an option or check the format from cv2 somehow
        # Opencv has an option to deliver all frames in a specified format - implement this and then we don't have to assume a format.
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #cut section from image 
        # [y1:y2, x1:x2, keep all the colors.]
            frame = frame[self.crop_Y1:self.crop_Y2, self.crop_X1:self.crop_X2, :]
        except:
            return
 
        if self.checkBoxLive.isChecked():
            self.widgetLiveView.show()
            self.widgetLiveView.setImage(frame)
        else:
            self.widgetLiveView.clearImage()
            self.widgetLiveView.hide()
        
        if self.checkBoxDigitizedView.isChecked():
            self.widgetDigitizedView.show()
        else:
            self.widgetDigitizedView.hide()
        
        self.widgetDigitizedView.setImage(frame)
        
        self.widgetGridView.updateGridSize(frame.shape[1],  frame.shape[0])
        self.widgetCursorControl.updateSize(frame.shape[1],  frame.shape[0])
    
    def settingChanged(self):
        self.updateOnCursorMove()
        self.settings.setValue("Multiplier_Selected",  self.comboBoxMultiplier.currentText())
        self.settings.setValue("Timebase_Selected",  self.comboBoxTimeBase.currentText())
        self.settings.setValue("VerticalDeflection_Selected",  self.comboBoxVerticalDeflection.currentText())
    
    def getVoltsPerDivision(self):
        multiplier = self.comboBoxMultiplier.currentData()
        VperDiv = multiplier * self.comboBoxVerticalDeflection.currentData()
        return VperDiv
        
    def getVoltsPerPixel(self):
        VoltsPerPixel = self.getVoltsPerDivision()  / self.widgetGridView.getPixelsPerDivision_Horizontal()
        return VoltsPerPixel
        
    def getSecondsPerPixel(self):
        return self.comboBoxTimeBase.currentData() / self.widgetGridView.getPixelsPerDivision_Vertical()
        
    def updateOnCursorMove(self):
        volts =  self.getVoltsPerPixel ()* abs (self.widgetCursorControl.getY1_pixels() - self.widgetCursorControl.getY2_pixels()) 
        volts = Quantity(volts, "V")
        self.labelVppDisplay.setText(str(volts))
        voltsDiv = Quantity(self.getVoltsPerDivision(), "V")
        self.labelVperDivDisplay.setText(str(voltsDiv))
        
        SecondsPerPixel = self.getSecondsPerPixel()
        deltaT = SecondsPerPixel * abs(self.widgetCursorControl.getX1_pixels() - self.widgetCursorControl.getX2_pixels())
        deltaT_inverse = 1/deltaT
        deltaT = Quantity(deltaT,  "s")
        deltaT_inverse = Quantity(deltaT_inverse, "Hz")
        self.labelDeltaTDisplay.setText(str(deltaT))
        self.labelTInverseDisplay.setText(str(deltaT_inverse))
        TperDiv = self.comboBoxTimeBase.currentData()
        TDiv = Quantity(TperDiv, "s")
        self.labelTperDivDisplay.setText(str(TDiv))
        
