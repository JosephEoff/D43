# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/DigitalD43/Forms/Grid.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Grid(object):
    def setupUi(self, Grid):
        Grid.setObjectName("Grid")
        Grid.resize(626, 472)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Grid)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Grid)
        QtCore.QMetaObject.connectSlotsByName(Grid)

    def retranslateUi(self, Grid):
        _translate = QtCore.QCoreApplication.translate
        Grid.setWindowTitle(_translate("Grid", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Grid = QtWidgets.QWidget()
    ui = Ui_Grid()
    ui.setupUi(Grid)
    Grid.show()
    sys.exit(app.exec_())

