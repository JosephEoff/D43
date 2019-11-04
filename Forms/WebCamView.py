from PyQt5 import  QtGui
from PyQt5.QtWidgets import QWidget
from Forms.Ui_WebCamView import Ui_WebCamView
import cv2

class WebCamView(QWidget, Ui_WebCamView):
    def __init__(self, parent):
            super(QWidget, self).__init__()
            
            self.setupUi(self)
            self.transparentThreshold = 0
            self.thresholdMode = cv2.THRESH_BINARY
            self.rescaled=False

    def clearImage(self):
        self.viewer.clear()
        
    def setImage(self, scopeImage):
        grayframe = cv2.cvtColor(scopeImage, cv2.COLOR_RGB2GRAY)
        ret, alpha = cv2.threshold(grayframe,  self.transparentThreshold, 255,  self.thresholdMode)
       
        b, g, r = cv2.split(scopeImage)
        rgba = [b,g,r, alpha]
        scopeImage= cv2.merge(rgba,4)
        img = QtGui.QImage(scopeImage, scopeImage.shape[1], scopeImage.shape[0], QtGui.QImage.Format_RGBA8888)
        pix = QtGui.QPixmap.fromImage(img)
        self.viewer.setPixmap(pix)

     
