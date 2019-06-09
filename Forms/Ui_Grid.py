# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joseph/EricProjects/D43/Forms/Grid.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Grid(object):
    def setupUi(self, Grid):
        Grid.setObjectName("Grid")
        Grid.resize(102, 78)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Grid.sizePolicy().hasHeightForWidth())
        Grid.setSizePolicy(sizePolicy)
        Grid.setMinimumSize(QtCore.QSize(50, 50))
        self.gridLayout = QtWidgets.QGridLayout(Grid)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

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

