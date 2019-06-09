from PyQt5.QtGui import QPainter,  QPen , QPixmap , QColor
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt,  QLineF,  pyqtSignal

from Forms.Ui_WebCamView import Ui_WebCamView
from Forms.Cursor_Enums import CursorType
from Forms.Cursor_Enums import CursorStyle
from Forms.Cursor import Cursor

class CursorControl(QWidget,  Ui_WebCamView):
    cursorMoved = pyqtSignal()
    
    def __init__(self, parent):
        super(QWidget, self).__init__()
        
        self.setupUi(self)
        self.parent=parent
        
        self.setMouseTracking(True)
        
        self.cursors = []
        self.barWidth= 5
        self.cursorWidth = self.width()
        self.cursorHeight = self.height()

        self.movingCursor = None
        
        self.cursor_T1 = None
        self.cursor_T2 = None
        self.cursor_V1 = None
        self.cursor_V2 = None
        self.cursor_zero = None
        self.addCursors()
        
        
    def addCursors(self):
        cursorColor = QColor(0, 186, 255, 100)
        cursorBarColor = QColor(0, 186, 255, 255)
        
        cursor = Cursor(15,  cursorColor,  cursorBarColor,  CursorType.horizontal,  CursorStyle.barred)
        self.addCursor(cursor)
        self.cursor_T1 = cursor
        
        cursor = Cursor(15,  cursorColor,  cursorBarColor,  CursorType.vertical,  CursorStyle.barred)
        self.addCursor(cursor)
        self.cursor_V1 = cursor
        
        cursor = Cursor(200,  cursorColor,  cursorBarColor,  CursorType.vertical,  CursorStyle.barred)
        self.addCursor(cursor)
        self.cursor_V2 = cursor
        
        cursor = Cursor(200,  cursorColor,  cursorBarColor,  CursorType.horizontal,  CursorStyle.barred)
        self.addCursor(cursor)
        self.cursor_T2 = cursor
        
        cursorColor = QColor(128, 128, 128, 100)
        cursorBarColor = QColor(128, 128, 128, 255)
        cursor = Cursor(200,  cursorColor,  cursorBarColor,  CursorType.zeroline,  CursorStyle.barred)
        self.addCursor(cursor)
        self.cursor_zero = cursor
        
    def getX1_pixels(self):
        return self.cursor_T1.getCursorPosition()
        
    def getX2_pixels(self):
        return self.cursor_T2.getCursorPosition()
        
    def getY1_pixels(self):
        return self.cursor_V1.getCursorPosition()
        
    def getY2_pixels(self):
        return self.cursor_V2.getCursorPosition()
        
    def getZero_pixels(self):
        return self.cursor_zero.getCursorPosition()
        
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
    
    def mouseReleaseEvent(self, event):
        if  event.button() == Qt.LeftButton:
            self.movingCursor = None
            event.ignore()
    
    def mouseMoveEvent(self, event):
        if self.movingCursor is None:
            return
        if not (event.buttons()  == Qt.LeftButton):
            event.ignore()
            return
        event.accept()
        self.changeCursorPosition(self.movingCursor,  event.pos())
        self.drawCursors()
        self.cursorMoved.emit()
        
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
        
        for cursor in self.cursors:
            if cursor.getType() == CursorType.vertical or  cursor.getType() == CursorType.zeroline:
                if cursor.getCursorPosition() > self.cursorHeight:
                    cursor.setCursorPosition(self.cursorHeight -2)
            if cursor.getType() == CursorType.horizontal:
                if cursor.getCursorPosition() > self.cursorWidth:
                    cursor.setCursorPosition(self.cursorWidth-2)
        
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
        if cursor.getType() == CursorType.vertical or  cursor.getType() == CursorType.zeroline:
            line = self.makeHorizontalLine(cursor.getCursorPosition())
        else:
            line = self.makeVerticalLine(cursor.getCursorPosition())
        return line
        
    def getBars(self, cursor):
        lines = []
        if cursor.getType() == CursorType.vertical or  cursor.getType() == CursorType.zeroline:
            line = self.makeHorizontalLine(cursor.getCursorPosition() + self.barWidth)
            lines.append(line)
            line = self.makeHorizontalLine(cursor.getCursorPosition() - self.barWidth)
            lines.append(line)
        elif cursor.getType() == CursorType.horizontal:
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
