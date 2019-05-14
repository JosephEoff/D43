from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from Forms.Ui_Grid import Ui_Grid

class Grid(QWidget, Ui_Grid):
    def __init__(self, parent):
            super(QWidget, self).__init__()
            self.pixelsPercm_H=45.7
            self.pixelsPercm_V=45.7
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawGrid(event, qp)
        qp.end()
        
    def drawGrid(self, event, qp):
        pen = QPen(QColor(255, 120, 0, 100), 2, Qt.SolidLine)
        qp.setPen(pen)
        cwidth=self.width()/2
        cheight= self.height()/2
        hcount=cwidth/self.pixelsPercm_H
        vcount=cheight/self.pixelsPercm_V
        for n in range(int(hcount+0.5)):
            xstep= n*self.pixelsPercm_H
            qp.drawLine(cwidth+xstep, 0, cwidth+xstep,  self.height())
            if n>0:
                qp.drawLine(cwidth-xstep, 0, cwidth-xstep,  self.height())
                
        for n in range(int(vcount+0.5)):
            ystep= n*self.pixelsPercm_H
            qp.drawLine(0, cheight+ystep,  self.width(),  cheight+ystep)
            if n>0:
                qp.drawLine(0, cheight-ystep,  self.width(),  cheight-ystep)
