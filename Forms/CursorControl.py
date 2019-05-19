from PyQt5.QtGui import QPainter,  QPen , QPixmap , QColor
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt,  QLineF

from Forms.Ui_WebCamView import Ui_WebCamView
from Forms.Cursor_Enums import CursorType
from Forms.Cursor_Enums import CursorStyle

class CursorControl(QWidget,  Ui_WebCamView):
    def __init__(self, parent):
        super(QWidget, self).__init__()
        
        self.setupUi(self)
        self.parent=parent
        self.cursors = []
        self.barWidth= 4
        self.cursorWidth = self.width()
        self.cursorHeight = self.height()
        self.setMouseTracking(True)
        self.movingCursor = None
        
    def mousePressEvent(self, event):
        if  not event.button() == Qt.LeftButton:
            self.movingCursor = None
            event.ignore()
            return
            
        cursor = self.getCursor(event.pos())
        if  cursor is None:
            event.ignore()
            return        
        self.movingCursor = cursor
        
    def mouseMoveEvent(self, event):
        if self.movingCursor is None:
            return
        if not (event.buttons()  == Qt.LeftButton):
            event.ignore()
            return
        event.accept()
        self.changeCursorPosition(self.movingCursor,  event.pos())
        self.drawCursors()
        
    def changeCursorPosition(self,  cursor,  eventPosition):
        x = eventPosition.x()
        y = eventPosition.y()
        if x<1:
            x = 1
            x = 1
        if y<1:
            y = 1
        if x > self.cursorWidth-2:
            x = self.cursorWidth-2
        if y > self.cursorHeight-2:
            y = self.cursorHeight -2
        if cursor.getType() == CursorType.horizontal:
            cursor.setCursorPosition(x)
        else:
            cursor.setCursorPosition(y)
        
    def getCursor(self,  eventPosition):
        for cursor in self.cursors:
            if self.closeToCursor(cursor,  eventPosition):
                return cursor
        return None
    
    def closeToCursor(self,  cursor,  position):
        if cursor.getType() == CursorType.horizontal:
            if abs(cursor.getCursorPosition() - position.x()) <= self.barWidth:
                return True
        else:
            if abs(cursor.getCursorPosition() - position.y()) <= self.barWidth:
                return True

    def updateSize(self,  width,  height):
        if self.cursorHeight == height and self.cursorWidth == width:
            return
        
        self.cursorHeight = height
        self.cursorWidth = width
        cursorPixmap = QPixmap(self.cursorWidth, self.cursorHeight)
        cursorPixmap.fill(QColor(255, 255, 255, 0))
        self.viewer.setPixmap(cursorPixmap)
        
    
    def addCursor(self,  cursor):
        self.cursors.append(cursor)
        self.drawCursors()
            
    def paintEvent(self, event):
        self.drawCursors()
        
    def drawCursors(self):        
        qp = QPainter()
        qp.begin(self)
        for cursor in self.cursors:               
            pen = QPen(cursor.getColor(), 1, Qt.SolidLine)
            qp.setPen(pen)
            line = self.getLine(cursor)
            qp.drawLine(line)
            if cursor.getStyle() == CursorStyle.barred:
                lines = self.getBars(cursor)
                pen = QPen(cursor.getBarColor(), 1, Qt.SolidLine)
                qp.setPen(pen)
                qp.drawLines(lines)
        qp.end()
    
    def getLine(self,  cursor):
        if cursor.getType() == CursorType.vertical:
            line = self.makeHorizontalLine(cursor.getCursorPosition())
        else:
            line = self.makeVerticalLine(cursor.getCursorPosition())
        return line
        
    def getBars(self, cursor):
        lines = []
        if cursor.getType() == CursorType.vertical:
            line = self.makeHorizontalLine(cursor.getCursorPosition() + self.barWidth)
            lines.append(line)
            line = self.makeHorizontalLine(cursor.getCursorPosition() - self.barWidth)
            lines.append(line)
        else:
            line = self.makeVerticalLine(cursor.getCursorPosition() + self.barWidth)
            lines.append(line)
            line = self.makeVerticalLine(cursor.getCursorPosition() - self.barWidth)
            lines.append(line)
            
        return lines
    
    def makeHorizontalLine(self,  position):
        line = QLineF(0,  position,  self.cursorWidth,  position)
        return line
    
    def makeVerticalLine(self,  position):
        line = QLineF(position,  0,  position,  self.cursorHeight)
        return line
