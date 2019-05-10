from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget
import cv2
from Forms.Ui_WebCamView import Ui_WebCamView

class WebCamView(QWidget, Ui_WebCamView):
    def __init__(self, parent):
            super(QWidget, self).__init__()
            
            self.setupUi(parent)
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
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
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
