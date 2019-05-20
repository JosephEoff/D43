from PyQt5 import QtCore, QtMultimedia
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
        self.widgetCursorControl.addCursors()
    
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
            frame = frame[65:498, 126:551, :]
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
        
