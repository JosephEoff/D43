from PyQt5 import  QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QLineF
from Forms.Ui_WebCamView import Ui_WebCamView
import numpy as np
import cv2

class DigitizerView(QWidget, Ui_WebCamView):
    def __init__(self, parent):
        super(QWidget, self).__init__()
        
        self.setupUi(self)
        self.range_X1 = 100
        self.range_X2 = 200
        self.lineMode = False
        self.traceColor = QtGui.QColor(255, 0, 0)
        self.ScopeImage = np.zeros((200, 200))
        self.DigitizedData = np.zeros((200, 200))
        
    def clearImage(self):
        self.viewer.clear()
    
    def setLineMode(self,  lineModeOn):
        self.lineMode=lineModeOn
        self.redrawImage()
    
    def setDigitizingRange(self,  X1,  X2):
        self.range_X1 = X1
        self.range_X2 = X2
    
    def setImage(self, scopeImage):
        self.ScopeImage = scopeImage
        self.redrawImage()
        
    def redrawImage(self):
        b, g, r = cv2.split(self.ScopeImage)
        digipix= QtGui.QPixmap(self.ScopeImage.shape[1], self.ScopeImage.shape[0])
        digipix.fill(QtGui.QColor(0, 0, 0, 0))
        spots = np.argmax(g, axis=0)
        
        self.DigitizedData = spots
        
        if self.lineMode:
            self.drawLines(spots,  digipix,  g)
        else:
            self.drawDots(spots,  digipix,  g)
        
        
    def drawDots(self, spots,  digipix,  phosphor):
        qp = QtGui.QPainter()
        qp.begin(digipix)
        qp.setPen(self.traceColor)
        for x in range(self.range_X1,  self.range_X2):
            qp.drawPoint(  x,  spots[x])
        qp.end()
    
        self.viewer.setPixmap(digipix)
        
    def drawLines(self, spots,  digipix,  phosphor):
        lines = []
        for x in range(self.range_X1,  self.range_X2):
            line = QLineF(x,  spots[x],  x+1,  spots[x+1])
            lines.append(line)
            
        qp = QtGui.QPainter()
        qp.begin(digipix)
        qp.setPen(self.traceColor)
        qp.drawLines(lines)
        qp.end()
    
        self.viewer.setPixmap(digipix)
        
    def getDigitizedData(self):
        return self.DigitizedData
    
    def getRange(self):
        return self.range_X1,  self.range_X2

