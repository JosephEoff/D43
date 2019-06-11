from PyQt5.QtGui import QPainter, QColor, QPen,  QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from Forms.Ui_WebCamView import Ui_WebCamView

class Grid(QWidget, Ui_WebCamView):
    def __init__(self, parent):
            super(QWidget, self).__init__()
            
            self.setupUi(self) 
            self.pixelsPercm_H=30
            self.pixelsPercm_V=30
            self.gridWidth = 100
            self.gridHeight = 100
            self.grid_X1 = 0
            self.grid_X2 = 100
            self.grid_Y1 = 0
            self.grid_Y2 = 100
            
    def paintEvent(self, event):
        self.drawGrid()
                
    def drawGrid(self):
        gridPixmap = QPixmap(self.gridWidth, self.gridHeight)
        gridPixmap.fill(QColor(255, 255, 255, 0))
        
        qp = QPainter()
        qp.begin(gridPixmap)
        pen = QPen(QColor(255, 120, 0, 100), 1, Qt.SolidLine)
        qp.setPen(pen)
        cwidth= (self.grid_X1 + self.grid_X2)/2
        cheight= (self.grid_Y1+self.grid_Y2)/2
        hcount=cwidth/self.pixelsPercm_H + 1
        vcount=cheight/self.pixelsPercm_V + 1
        
        for n in range(int(hcount+0.5)):
            xstep= n*self.pixelsPercm_H
            qp.drawLine(cwidth+xstep, 0, cwidth+xstep,  self.gridHeight)
            if n>0:
                qp.drawLine(cwidth-xstep, 0, cwidth-xstep,  self.gridHeight)
                
        for n in range(int(vcount+0.5)):
            ystep= n*self.pixelsPercm_H
            qp.drawLine(0, cheight+ystep,  self.gridWidth,  cheight+ystep)
            if n>0:
                qp.drawLine(0, cheight-ystep,  self.gridWidth,  cheight-ystep)
                
        #Border around the display 
        pen = QPen(QColor(255, 255, 255, 100), 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(0, 0,  self.gridWidth-1,  0)
        qp.drawLine(0, self.gridHeight-1,  self.gridWidth-1,  self.gridHeight-1)
        qp.drawLine(0, 0,  0,  self.gridHeight-1)
        qp.drawLine(self.gridWidth-1, 0,  self.gridWidth-1,  self.gridHeight-1)
        
        qp.end()
        self.viewer.setPixmap(gridPixmap)

    def updateGridSize(self,  width,  height):
        if self.gridHeight == height and self.gridWidth == width:
            return
        self.gridHeight = height
        self.gridWidth = width
        self.drawGrid()
    
    def updateGridSpacing(self,  X1,  X2,  Y1,  Y2,  horizontalDivisions,  verticalDivisions):
        self.grid_X1 = X1
        self.grid_X2 = X2
        self.grid_Y1 = Y1
        self.grid_Y2 = Y2
        self.pixelsPercm_H = abs(X2- X1)/horizontalDivisions
        self.pixelsPercm_V = abs(Y2-Y1)/verticalDivisions
        self.drawGrid()
        
    def getPixelsPerDivision_Horizontal(self):
        return self.pixelsPercm_H
    
    def getPixelsPerDivision_Vertical(self):
        return self.pixelsPercm_V
    
        
