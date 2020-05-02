from PyQt5 import  QtGui
from PyQt5.QtWidgets import QWidget
from Forms.Ui_WebCamView import Ui_WebCamView
import numpy as np
import cv2

class WebCamView(QWidget, Ui_WebCamView):
    def __init__(self, parent):
            super(QWidget, self).__init__()
            
            self.setupUi(self)
            self.transparentThreshold = 0
            self.thresholdMode = cv2.THRESH_BINARY
            self.rescaled=False
            self.persist = False
            self.persistImage = None

    def clearImage(self):
        self.viewer.clear()
    
    def setPersist(self, persistOn):
        self.persist = persistOn
    
    def setImage(self, scopeImage):
        grayframe = cv2.cvtColor(scopeImage, cv2.COLOR_RGB2GRAY)
        ret, alpha = cv2.threshold(grayframe,  self.transparentThreshold, 255,  self.thresholdMode)
       
        b, g, r = cv2.split(scopeImage)
        rgba = [b,g,r, alpha]
        scopeImage= cv2.merge(rgba,4)
        if self.persist:
            scopeImage = self.doImagePersistance(scopeImage,  g)
            
        img = QtGui.QImage(scopeImage, scopeImage.shape[1], scopeImage.shape[0], QtGui.QImage.Format_RGBA8888)
        pix = QtGui.QPixmap.fromImage(img)
        self.viewer.setPixmap(pix)

    def doImagePersistance(self,  scopeImage,  green):
        if self.persistImage is None:
            self.persistImage = scopeImage
            return scopeImage
        
        if  self.persistImage.shape != scopeImage.shape:
            self.persistImage = scopeImage
        
        threshold = np.amax(self.persistImage[:, :, 1]) * 0.8
        bright = np.where(green.min(0) >= threshold)[0]
        if bright.size>0:
            for x in np.nditer(bright):
                self.persistImage[:, x] = scopeImage[:, x]
            
        return self.persistImage
        
        
