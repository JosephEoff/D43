# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/DigitalD43/Forms/WebCamView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WebCamView(object):
    def setupUi(self, WebCamView):
        WebCamView.setObjectName("WebCamView")
        WebCamView.resize(102, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WebCamView.sizePolicy().hasHeightForWidth())
        WebCamView.setSizePolicy(sizePolicy)
        WebCamView.setMinimumSize(QtCore.QSize(50, 50))
        self.gridLayout = QtWidgets.QGridLayout(WebCamView)
        self.gridLayout.setObjectName("gridLayout")
        self.viewer = QtWidgets.QLabel(WebCamView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewer.sizePolicy().hasHeightForWidth())
        self.viewer.setSizePolicy(sizePolicy)
        self.viewer.setMinimumSize(QtCore.QSize(50, 50))
        self.viewer.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.viewer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.viewer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.viewer.setLineWidth(0)
        self.viewer.setText("")
        self.viewer.setObjectName("viewer")
        self.gridLayout.addWidget(self.viewer, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.retranslateUi(WebCamView)
        QtCore.QMetaObject.connectSlotsByName(WebCamView)

    def retranslateUi(self, WebCamView):
        _translate = QtCore.QCoreApplication.translate
        WebCamView.setWindowTitle(_translate("WebCamView", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WebCamView = QtWidgets.QWidget()
    ui = Ui_WebCamView()
    ui.setupUi(WebCamView)
    WebCamView.show()
    sys.exit(app.exec_())

