from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget
import cv2
from Forms.Ui_WebCamView import Ui_WebCamView
import numpy as np

class WebCamView(QWidget, Ui_WebCamView):
    def __init__(self, parent):
            super(QWidget, self).__init__()
            
            self.setupUi(parent)
            self.transparentThreshold = 20
            self.thresholdMode = cv2.THRESH_BINARY
            self.fps = 24
            self.videocapture = cv2.VideoCapture(0)
            self.videocapture.set(3,1024)
            self.videocapture.set(4,768)
            self.start()

    def nextFrameSlot(self):
        ret, frame = self.videocapture.read()

        # Assume Webcam gives BGR format images
        # May need to add an option or check the format from cv2 somehow
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        grayimage = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        
        ret, alpha = cv2.threshold(grayimage,  self.transparentThreshold, 255,  self.thresholdMode)
        b, g, r = cv2.split(frame)
        rgba = [b,g,r, alpha]
        frame = cv2.merge(rgba,4)
 
       
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGBA8888)
  
        pix = QtGui.QPixmap.fromImage(img)
        self.viewer.resize(pix.size().width(),  pix.size().height())
        self.resize(pix.size().width(),  pix.size().height())
       # self.adjustSize()
        self.viewer.setPixmap(pix)
        
    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./self.fps)

    def stop(self):
        self.timer.stop()
        
    def useBinaryTransparentMode(self, useBinaryMode):
        if useBinaryMode:
            self.thresholdMode = cv2.THRESH_BINARY
        else:
            self.thresholdMode = cv2.THRESH_TOZERO
    
    def setThresholdLevel(self, level):
        if level>=0 and level<=255:
            self.transparentThreshold = level
            
