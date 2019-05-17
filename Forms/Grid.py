from PyQt5.QtGui import QPainter, QColor, QPen,  QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from Forms.Ui_WebCamView import Ui_WebCamView

class Grid(QWidget, Ui_WebCamView):
    def __init__(self, parent):
            super(QWidget, self).__init__()
            
            self.setupUi(self) 
            self.pixelsPercm_H=45.7
            self.pixelsPercm_V=45.7
            self.gridWidth = 100
            self.gridHeight = 100
                
    def drawGrid(self):
        gridPixmap = QPixmap(self.gridWidth, self.gridHeight)
        gridPixmap.fill(QColor(255, 255, 255, 0))
        
        qp = QPainter()
        qp.begin(gridPixmap)
        pen = QPen(QColor(255, 120, 0, 100), 1, Qt.SolidLine)
        qp.setPen(pen)
        cwidth=self.gridWidth/2
        cheight= self.gridHeight/2
        hcount=cwidth/self.pixelsPercm_H
        vcount=cheight/self.pixelsPercm_V
        
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
        
        qp.end()
        self.viewer.setPixmap(gridPixmap)

    def updateGridSize(self,  width,  height):
        if self.gridHeight == height and self.gridWidth == width:
            return
        self.gridHeight = height
        self.gridWidth = width
        self.drawGrid()
    
    def updateGridSpacing(self,  pixelsPercm_H,  pixelsPerc_V):
        self.pixelsPercm_H=pixelsPercm_H
        self.pixelsPercm_V=pixelsPerc_V
        self.drawGrid()
    
        
