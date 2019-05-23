from PyQt5 import  QtGui
from PyQt5.QtWidgets import QWidget
from Forms.Ui_WebCamView import Ui_WebCamView
import numpy as np
import cv2

class DigitizerView(QWidget, Ui_WebCamView):
    def __init__(self, parent):
        super(QWidget, self).__init__()
        
        self.setupUi(self)
        self.range_X1 = 100
        self.range_X2 = 200
    def clearImage(self):
        self.viewer.clear()
    
    def setDigitizingRange(self,  X1,  X2):
        self.range_X1 = X1
        self.range_X2 = X2
    
    def setImage(self, scopeImage):
        b, g, r = cv2.split(scopeImage)
        digipix= QtGui.QPixmap(scopeImage.shape[1], scopeImage.shape[0])
        digipix.fill(QtGui.QColor(0, 0, 0, 0))
        spots = np.argmax(g, axis=0)
    
        qp = QtGui.QPainter()
        qp.begin(digipix)
        qp.setPen(QtGui.QColor(255, 0, 0))
        for x in range(self.range_X1,  self.range_X2):
            if g[spots[x],  x]>=5:
                qp.drawPoint(  x,  spots[x])
        qp.end()
    
        self.viewer.setPixmap(digipix)

