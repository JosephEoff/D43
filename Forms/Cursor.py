from PyQt5.QtGui import QColor

from Forms.Cursor_Enums import CursorType
from Forms.Cursor_Enums import CursorStyle

class Cursor():
        def __init__(self, position,  cursorColor,  cursorBarColor,  cursorType = CursorType.horizontal,  cursorStyle = CursorStyle.barred ):         
            self.cursorType = cursorType
            self.cursorStyle = cursorStyle
            self.cursorPosition = position
            
            self.cursorColor = QColor()
            self.cursorBarColor = QColor()
            self.cursorColor = cursorColor
            self.cursorBarColor = cursorBarColor

        
        def setCursorPosition(self, newPosition):
            self.cursorPosition = newPosition
        
        def getCursorPosition(self):
            return self.cursorPosition
            
        def getStyle(self):
            return self.cursorStyle
            
        def getType(self):
            return self.cursorType
            
        def getColor(self):
            return self.cursorColor
        
        def getBarColor(self):
            return self.cursorBarColor
