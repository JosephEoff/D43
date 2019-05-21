from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QWidget
import cv2
from Forms.Ui_Controls import Ui_Controls

class Controls(QWidget, Ui_Controls):
    def __init__(self, parent):
        super(QWidget, self).__init__()
                
        self.transparentThreshold = 20
        self.thresholdMode = cv2.THRESH_BINARY
        self.fps = 24
        self.videocapture = None 
        self.setupUi(self)
        self.groupBoxCalibration.hide()
        self.availableCameras = self.getListOfCameras()
        self.comboBoxCameraSelect.addItems(self.availableCameras)
        self.radioButtonRun.toggled.connect(self.doRun)
        self.comboBoxCameraSelect.currentIndexChanged.connect(self.changeCamera)
        self.pushButtonCrop.clicked.connect(self.on_buttonCropClicked)
        self.pushButtonReset.clicked.connect(self.on_buttonResetClicked)
        
        self.settings = QSettings()
        self.rawImageWidth = int(self.settings.value("rawImageWidth",  640))
        self.rawImageHeight = int(self.settings.value("rawImageHeight",  480))
        self.crop_X1 = int(self.settings.value("crop_X1",  0))
        self.crop_X2 = int(self.settings.value("crop_X2",  640))
        self.crop_Y1 = int(self.settings.value("crop_Y1",  0))
        self.crop_Y2 = int(self.settings.value("crop_Y2",  480))

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
    
    def on_buttonResetClicked(self):
        self.crop_X1 = 0
        self.crop_X2 = self.rawImageWidth
        self.crop_Y1 = 0
        self.crop_Y2 = self.rawImageHeight
    
    def doRun(self):
        if self.radioButtonRun.isChecked():
            self.start()
        else:
            self.stop()
    
    def changeCamera(self, selectedCameraIndex):
        self.stop()
        self.doRun()
    
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
                return
        # Assume Webcam gives BGR format images
        # May need to add an option or check the format from cv2 somehow
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #cut section from image 
        # [y1:y2, x1:x2, keep all the colors.]
            frame = frame[self.crop_Y1:self.crop_Y2, self.crop_X1:self.crop_X2, :]
        except:
           return
 
        if self.checkBoxLive.isChecked():
            self.widgetLiveView.setImage(frame)
        else:
            self.widgetLiveView.clearImage()
        
        if self.checkBoxDigitizedView.isChecked():
            self.widgetDigitizedView.setImage(frame)
        else:
            self.widgetDigitizedView.clearImage()
            
        self.widgetGridView.updateGridSize(frame.shape[1],  frame.shape[0])
        self.widgetCursorControl.updateSize(frame.shape[1],  frame.shape[0])
        
