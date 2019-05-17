from PyQt5 import  QtGui
from PyQt5.QtWidgets import QWidget
from Forms.Ui_WebCamView import Ui_WebCamView
import numpy as np
import cv2

class DigitizerView(QWidget, Ui_WebCamView):
    def __init__(self, parent):
        super(QWidget, self).__init__()
            
        self.setupUi(parent)
    
    def clearImage(self):
        self.viewer.clear()
    
    def setImage(self, scopeImage):
        b, g, r = cv2.split(scopeImage)
        digipix= QtGui.QPixmap(scopeImage.shape[1], scopeImage.shape[0])
        digipix.fill(QtGui.QColor(0, 0, 0, 0))
        spots = np.argmax(g, 0)
    
        qp = QtGui.QPainter()
        qp.begin(digipix)
        qp.setPen(QtGui.QColor(255, 0, 0))
        for x in range(scopeImage.shape[0]):
            if g[x, spots[x]]>=5:
                qp.drawPoint(x, spots[x])
        qp.end()
        
        self.viewer.setPixmap(digipix)
        self.viewer.resize(self.viewer.minimumSizeHint() )#pix.size().width(),  pix.size().height())
      
        #self.resize(self.minimumSizeHint())
       
