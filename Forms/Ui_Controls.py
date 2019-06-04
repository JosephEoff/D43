# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/DigitalD43/Forms/Controls.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Controls(object):
    def setupUi(self, Controls):
        Controls.setObjectName("Controls")
        Controls.resize(424, 608)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Controls.sizePolicy().hasHeightForWidth())
        Controls.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QtWidgets.QGridLayout(Controls)
        self.gridLayout_6.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.layoutScope = QtWidgets.QGridLayout()
        self.layoutScope.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.layoutScope.setContentsMargins(0, 0, 0, 0)
        self.layoutScope.setSpacing(0)
        self.layoutScope.setObjectName("layoutScope")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxDisplay = QtWidgets.QGroupBox(Controls)
        self.groupBoxDisplay.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.groupBoxDisplay.setObjectName("groupBoxDisplay")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxDisplay)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_Display = QtWidgets.QGridLayout()
        self.gridLayout_Display.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_Display.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Display.setSpacing(0)
        self.gridLayout_Display.setObjectName("gridLayout_Display")
        self.widgetLiveView = WebCamView(self.groupBoxDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetLiveView.sizePolicy().hasHeightForWidth())
        self.widgetLiveView.setSizePolicy(sizePolicy)
        self.widgetLiveView.setMinimumSize(QtCore.QSize(50, 50))
        self.widgetLiveView.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widgetLiveView.setObjectName("widgetLiveView")
        self.gridLayout_Display.addWidget(self.widgetLiveView, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.widgetGridView = Grid(self.groupBoxDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetGridView.sizePolicy().hasHeightForWidth())
        self.widgetGridView.setSizePolicy(sizePolicy)
        self.widgetGridView.setMinimumSize(QtCore.QSize(50, 50))
        self.widgetGridView.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widgetGridView.setObjectName("widgetGridView")
        self.gridLayout_Display.addWidget(self.widgetGridView, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.widgetDigitizedView = DigitizerView(self.groupBoxDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetDigitizedView.sizePolicy().hasHeightForWidth())
        self.widgetDigitizedView.setSizePolicy(sizePolicy)
        self.widgetDigitizedView.setMinimumSize(QtCore.QSize(50, 50))
        self.widgetDigitizedView.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widgetDigitizedView.setObjectName("widgetDigitizedView")
        self.gridLayout_Display.addWidget(self.widgetDigitizedView, 0, 0, 1, 1)
        self.widgetCursorControl = CursorControl(self.groupBoxDisplay)
        self.widgetCursorControl.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetCursorControl.sizePolicy().hasHeightForWidth())
        self.widgetCursorControl.setSizePolicy(sizePolicy)
        self.widgetCursorControl.setMinimumSize(QtCore.QSize(50, 50))
        self.widgetCursorControl.setAutoFillBackground(False)
        self.widgetCursorControl.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widgetCursorControl.setObjectName("widgetCursorControl")
        self.gridLayout_Display.addWidget(self.widgetCursorControl, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_Display)
        self.groupBoxMeasurements = QtWidgets.QGroupBox(self.groupBoxDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxMeasurements.sizePolicy().hasHeightForWidth())
        self.groupBoxMeasurements.setSizePolicy(sizePolicy)
        self.groupBoxMeasurements.setTitle("")
        self.groupBoxMeasurements.setFlat(True)
        self.groupBoxMeasurements.setObjectName("groupBoxMeasurements")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBoxMeasurements)
        self.gridLayout_11.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_11.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_11.setSpacing(1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.groupBoxTime = QtWidgets.QGroupBox(self.groupBoxMeasurements)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxTime.sizePolicy().hasHeightForWidth())
        self.groupBoxTime.setSizePolicy(sizePolicy)
        self.groupBoxTime.setTitle("")
        self.groupBoxTime.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBoxTime.setFlat(True)
        self.groupBoxTime.setObjectName("groupBoxTime")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBoxTime)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelDeltaT = QtWidgets.QLabel(self.groupBoxTime)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDeltaT.sizePolicy().hasHeightForWidth())
        self.labelDeltaT.setSizePolicy(sizePolicy)
        self.labelDeltaT.setStyleSheet("color: rgb(0, 255, 255);")
        self.labelDeltaT.setObjectName("labelDeltaT")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelDeltaT)
        self.labelDeltaTDisplay = QtWidgets.QLabel(self.groupBoxTime)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDeltaTDisplay.sizePolicy().hasHeightForWidth())
        self.labelDeltaTDisplay.setSizePolicy(sizePolicy)
        self.labelDeltaTDisplay.setStyleSheet("color: rgb(0, 255, 255);")
        self.labelDeltaTDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDeltaTDisplay.setObjectName("labelDeltaTDisplay")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelDeltaTDisplay)
        self.labelTInverse = QtWidgets.QLabel(self.groupBoxTime)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTInverse.sizePolicy().hasHeightForWidth())
        self.labelTInverse.setSizePolicy(sizePolicy)
        self.labelTInverse.setStyleSheet("color: rgb(0, 255, 255);")
        self.labelTInverse.setObjectName("labelTInverse")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelTInverse)
        self.labelTInverseDisplay = QtWidgets.QLabel(self.groupBoxTime)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTInverseDisplay.sizePolicy().hasHeightForWidth())
        self.labelTInverseDisplay.setSizePolicy(sizePolicy)
        self.labelTInverseDisplay.setStyleSheet("color: rgb(0, 255, 255);")
        self.labelTInverseDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTInverseDisplay.setObjectName("labelTInverseDisplay")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelTInverseDisplay)
        self.labelF = QtWidgets.QLabel(self.groupBoxTime)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelF.sizePolicy().hasHeightForWidth())
        self.labelF.setSizePolicy(sizePolicy)
        self.labelF.setStyleSheet("color: rgb(0, 255, 255);")
        self.labelF.setObjectName("labelF")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelF)
        self.labelFDisplay = QtWidgets.QLabel(self.groupBoxTime)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFDisplay.sizePolicy().hasHeightForWidth())
        self.labelFDisplay.setSizePolicy(sizePolicy)
        self.labelFDisplay.setStyleSheet("color: rgb(0, 255, 255);")
        self.labelFDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelFDisplay.setObjectName("labelFDisplay")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelFDisplay)
        self.gridLayout_11.addWidget(self.groupBoxTime, 0, 0, 1, 1)
        self.groupBoxVoltage = QtWidgets.QGroupBox(self.groupBoxMeasurements)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxVoltage.sizePolicy().hasHeightForWidth())
        self.groupBoxVoltage.setSizePolicy(sizePolicy)
        self.groupBoxVoltage.setTitle("")
        self.groupBoxVoltage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.groupBoxVoltage.setFlat(True)
        self.groupBoxVoltage.setObjectName("groupBoxVoltage")
        self.formLayout = QtWidgets.QFormLayout(self.groupBoxVoltage)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.labelVpp = QtWidgets.QLabel(self.groupBoxVoltage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVpp.sizePolicy().hasHeightForWidth())
        self.labelVpp.setSizePolicy(sizePolicy)
        self.labelVpp.setStyleSheet("color: rgb(0, 255, 255);")
        self.labelVpp.setObjectName("labelVpp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelVpp)
        self.labelVppDisplay = QtWidgets.QLabel(self.groupBoxVoltage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVppDisplay.sizePolicy().hasHeightForWidth())
        self.labelVppDisplay.setSizePolicy(sizePolicy)
        self.labelVppDisplay.setStyleSheet("color: rgb(0, 255, 255);")
        self.labelVppDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelVppDisplay.setObjectName("labelVppDisplay")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelVppDisplay)
        self.gridLayout_11.addWidget(self.groupBoxVoltage, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBoxMeasurements)
        self.verticalLayout.addWidget(self.groupBoxDisplay)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.layoutScope.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.layoutControls = QtWidgets.QGridLayout()
        self.layoutControls.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.layoutControls.setContentsMargins(0, 0, 0, 0)
        self.layoutControls.setSpacing(0)
        self.layoutControls.setObjectName("layoutControls")
        self.groupBoxSettings = QtWidgets.QGroupBox(Controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxSettings.sizePolicy().hasHeightForWidth())
        self.groupBoxSettings.setSizePolicy(sizePolicy)
        self.groupBoxSettings.setObjectName("groupBoxSettings")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxSettings)
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBoxTimeBase = QtWidgets.QComboBox(self.groupBoxSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxTimeBase.sizePolicy().hasHeightForWidth())
        self.comboBoxTimeBase.setSizePolicy(sizePolicy)
        self.comboBoxTimeBase.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBoxTimeBase.setFrame(True)
        self.comboBoxTimeBase.setObjectName("comboBoxTimeBase")
        self.gridLayout_3.addWidget(self.comboBoxTimeBase, 0, 0, 1, 1)
        self.labelTimeBase = QtWidgets.QLabel(self.groupBoxSettings)
        self.labelTimeBase.setObjectName("labelTimeBase")
        self.gridLayout_3.addWidget(self.labelTimeBase, 0, 2, 1, 1)
        self.comboBoxVerticalDeflection = QtWidgets.QComboBox(self.groupBoxSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxVerticalDeflection.sizePolicy().hasHeightForWidth())
        self.comboBoxVerticalDeflection.setSizePolicy(sizePolicy)
        self.comboBoxVerticalDeflection.setObjectName("comboBoxVerticalDeflection")
        self.gridLayout_3.addWidget(self.comboBoxVerticalDeflection, 1, 0, 1, 1)
        self.labelVerticalDeflection = QtWidgets.QLabel(self.groupBoxSettings)
        self.labelVerticalDeflection.setObjectName("labelVerticalDeflection")
        self.gridLayout_3.addWidget(self.labelVerticalDeflection, 1, 2, 1, 1)
        self.labelMultiplier = QtWidgets.QLabel(self.groupBoxSettings)
        self.labelMultiplier.setObjectName("labelMultiplier")
        self.gridLayout_3.addWidget(self.labelMultiplier, 2, 2, 1, 1)
        self.comboBoxMultiplier = QtWidgets.QComboBox(self.groupBoxSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxMultiplier.sizePolicy().hasHeightForWidth())
        self.comboBoxMultiplier.setSizePolicy(sizePolicy)
        self.comboBoxMultiplier.setObjectName("comboBoxMultiplier")
        self.gridLayout_3.addWidget(self.comboBoxMultiplier, 2, 0, 1, 1)
        self.layoutControls.addWidget(self.groupBoxSettings, 0, 0, 1, 1)
        self.groupBoxMeasurement = QtWidgets.QGroupBox(Controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxMeasurement.sizePolicy().hasHeightForWidth())
        self.groupBoxMeasurement.setSizePolicy(sizePolicy)
        self.groupBoxMeasurement.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBoxMeasurement.setFlat(False)
        self.groupBoxMeasurement.setObjectName("groupBoxMeasurement")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBoxMeasurement)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setSpacing(0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.spinBoxSelectedCycles = QtWidgets.QSpinBox(self.groupBoxMeasurement)
        self.spinBoxSelectedCycles.setMinimum(1)
        self.spinBoxSelectedCycles.setMaximum(20)
        self.spinBoxSelectedCycles.setProperty("value", 1)
        self.spinBoxSelectedCycles.setObjectName("spinBoxSelectedCycles")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.spinBoxSelectedCycles)
        self.labelSelectedCycles = QtWidgets.QLabel(self.groupBoxMeasurement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSelectedCycles.sizePolicy().hasHeightForWidth())
        self.labelSelectedCycles.setSizePolicy(sizePolicy)
        self.labelSelectedCycles.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSelectedCycles.setObjectName("labelSelectedCycles")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelSelectedCycles)
        self.layoutControls.addWidget(self.groupBoxMeasurement, 1, 0, 1, 1)
        self.groupBoxView = QtWidgets.QGroupBox(Controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxView.sizePolicy().hasHeightForWidth())
        self.groupBoxView.setSizePolicy(sizePolicy)
        self.groupBoxView.setObjectName("groupBoxView")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxView)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBoxLive = QtWidgets.QCheckBox(self.groupBoxView)
        self.checkBoxLive.setChecked(True)
        self.checkBoxLive.setObjectName("checkBoxLive")
        self.gridLayout_5.addWidget(self.checkBoxLive, 2, 0, 1, 1)
        self.checkBoxDigitizedView = QtWidgets.QCheckBox(self.groupBoxView)
        self.checkBoxDigitizedView.setObjectName("checkBoxDigitizedView")
        self.gridLayout_5.addWidget(self.checkBoxDigitizedView, 2, 1, 1, 1)
        self.checkBoxLines = QtWidgets.QCheckBox(self.groupBoxView)
        self.checkBoxLines.setObjectName("checkBoxLines")
        self.gridLayout_5.addWidget(self.checkBoxLines, 3, 1, 1, 1)
        self.layoutControls.addWidget(self.groupBoxView, 2, 0, 1, 1)
        self.groupBoxStorage = QtWidgets.QGroupBox(Controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxStorage.sizePolicy().hasHeightForWidth())
        self.groupBoxStorage.setSizePolicy(sizePolicy)
        self.groupBoxStorage.setObjectName("groupBoxStorage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxStorage)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonSnapshot = QtWidgets.QPushButton(self.groupBoxStorage)
        self.pushButtonSnapshot.setObjectName("pushButtonSnapshot")
        self.gridLayout_4.addWidget(self.pushButtonSnapshot, 1, 0, 1, 1)
        self.pushButtonDigitizedData = QtWidgets.QPushButton(self.groupBoxStorage)
        self.pushButtonDigitizedData.setObjectName("pushButtonDigitizedData")
        self.gridLayout_4.addWidget(self.pushButtonDigitizedData, 1, 1, 1, 1)
        self.checkBoxPause = QtWidgets.QCheckBox(self.groupBoxStorage)
        self.checkBoxPause.setObjectName("checkBoxPause")
        self.gridLayout_4.addWidget(self.checkBoxPause, 0, 0, 1, 1)
        self.layoutControls.addWidget(self.groupBoxStorage, 3, 0, 1, 1)
        self.groupBoxSetup = QtWidgets.QGroupBox(Controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxSetup.sizePolicy().hasHeightForWidth())
        self.groupBoxSetup.setSizePolicy(sizePolicy)
        self.groupBoxSetup.setObjectName("groupBoxSetup")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxSetup)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxShowCalibration = QtWidgets.QCheckBox(self.groupBoxSetup)
        self.checkBoxShowCalibration.setObjectName("checkBoxShowCalibration")
        self.gridLayout.addWidget(self.checkBoxShowCalibration, 0, 0, 1, 1)
        self.comboBoxCameraSelect = QtWidgets.QComboBox(self.groupBoxSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCameraSelect.sizePolicy().hasHeightForWidth())
        self.comboBoxCameraSelect.setSizePolicy(sizePolicy)
        self.comboBoxCameraSelect.setObjectName("comboBoxCameraSelect")
        self.gridLayout.addWidget(self.comboBoxCameraSelect, 0, 1, 1, 1)
        self.layoutControls.addWidget(self.groupBoxSetup, 4, 0, 1, 1)
        self.groupBoxCalibration = QtWidgets.QGroupBox(Controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxCalibration.sizePolicy().hasHeightForWidth())
        self.groupBoxCalibration.setSizePolicy(sizePolicy)
        self.groupBoxCalibration.setObjectName("groupBoxCalibration")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxCalibration)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelHorizontalDivisions = QtWidgets.QLabel(self.groupBoxCalibration)
        self.labelHorizontalDivisions.setObjectName("labelHorizontalDivisions")
        self.gridLayout_2.addWidget(self.labelHorizontalDivisions, 1, 1, 1, 1)
        self.spinBoxHorizontalDivisions = QtWidgets.QSpinBox(self.groupBoxCalibration)
        self.spinBoxHorizontalDivisions.setMinimum(1)
        self.spinBoxHorizontalDivisions.setMaximum(15)
        self.spinBoxHorizontalDivisions.setObjectName("spinBoxHorizontalDivisions")
        self.gridLayout_2.addWidget(self.spinBoxHorizontalDivisions, 1, 3, 1, 1)
        self.pushButtonReset = QtWidgets.QPushButton(self.groupBoxCalibration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonReset.sizePolicy().hasHeightForWidth())
        self.pushButtonReset.setSizePolicy(sizePolicy)
        self.pushButtonReset.setObjectName("pushButtonReset")
        self.gridLayout_2.addWidget(self.pushButtonReset, 0, 3, 1, 1)
        self.pushButtonCrop = QtWidgets.QPushButton(self.groupBoxCalibration)
        self.pushButtonCrop.setObjectName("pushButtonCrop")
        self.gridLayout_2.addWidget(self.pushButtonCrop, 0, 1, 1, 1)
        self.spinBoxVerticalDivisions = QtWidgets.QSpinBox(self.groupBoxCalibration)
        self.spinBoxVerticalDivisions.setMinimum(1)
        self.spinBoxVerticalDivisions.setMaximum(15)
        self.spinBoxVerticalDivisions.setObjectName("spinBoxVerticalDivisions")
        self.gridLayout_2.addWidget(self.spinBoxVerticalDivisions, 2, 3, 1, 1)
        self.labelVerticalDivisions = QtWidgets.QLabel(self.groupBoxCalibration)
        self.labelVerticalDivisions.setObjectName("labelVerticalDivisions")
        self.gridLayout_2.addWidget(self.labelVerticalDivisions, 2, 1, 1, 1)
        self.pushButtonGrid = QtWidgets.QPushButton(self.groupBoxCalibration)
        self.pushButtonGrid.setObjectName("pushButtonGrid")
        self.gridLayout_2.addWidget(self.pushButtonGrid, 3, 1, 1, 1)
        self.layoutControls.addWidget(self.groupBoxCalibration, 5, 0, 1, 1)
        self.layoutScope.addLayout(self.layoutControls, 0, 3, 1, 1)
        self.gridLayout_6.addLayout(self.layoutScope, 0, 1, 1, 1)

        self.retranslateUi(Controls)
        self.checkBoxShowCalibration.toggled['bool'].connect(self.groupBoxCalibration.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Controls)

    def retranslateUi(self, Controls):
        _translate = QtCore.QCoreApplication.translate
        Controls.setWindowTitle(_translate("Controls", "Form"))
        self.labelDeltaT.setText(_translate("Controls", "T"))
        self.labelDeltaTDisplay.setText(_translate("Controls", "0"))
        self.labelTInverse.setText(_translate("Controls", "1/T"))
        self.labelTInverseDisplay.setText(_translate("Controls", "0"))
        self.labelF.setText(_translate("Controls", "F"))
        self.labelFDisplay.setText(_translate("Controls", "0"))
        self.labelVpp.setText(_translate("Controls", "Vpp"))
        self.labelVppDisplay.setText(_translate("Controls", "0"))
        self.groupBoxSettings.setTitle(_translate("Controls", "Settings"))
        self.comboBoxTimeBase.setToolTip(_translate("Controls", "Seconds per centimeter"))
        self.labelTimeBase.setText(_translate("Controls", "Timebase"))
        self.labelVerticalDeflection.setText(_translate("Controls", "Vertical deflection"))
        self.labelMultiplier.setText(_translate("Controls", "Multiplier"))
        self.groupBoxMeasurement.setTitle(_translate("Controls", "Measurement"))
        self.labelSelectedCycles.setText(_translate("Controls", "Selected cycles (frequency counter)"))
        self.groupBoxView.setTitle(_translate("Controls", "View"))
        self.checkBoxLive.setText(_translate("Controls", "Live"))
        self.checkBoxDigitizedView.setText(_translate("Controls", "Digitized"))
        self.checkBoxLines.setText(_translate("Controls", "Lines"))
        self.groupBoxStorage.setTitle(_translate("Controls", "Storage"))
        self.pushButtonSnapshot.setText(_translate("Controls", "Snapshot"))
        self.pushButtonDigitizedData.setText(_translate("Controls", "Digitized Data"))
        self.checkBoxPause.setText(_translate("Controls", "Pause"))
        self.groupBoxSetup.setTitle(_translate("Controls", "Setup"))
        self.checkBoxShowCalibration.setText(_translate("Controls", "Calibrate"))
        self.groupBoxCalibration.setTitle(_translate("Controls", "Calibration"))
        self.labelHorizontalDivisions.setText(_translate("Controls", "Horizontal Divisions"))
        self.pushButtonReset.setText(_translate("Controls", "Reset"))
        self.pushButtonCrop.setText(_translate("Controls", "Crop"))
        self.labelVerticalDivisions.setText(_translate("Controls", "Vertical Divisions"))
        self.pushButtonGrid.setText(_translate("Controls", "Grid"))

from Forms.CursorControl import CursorControl
from Forms.DigitizerView import DigitizerView
from Forms.Grid import Grid
from Forms.WebCamView import WebCamView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Controls = QtWidgets.QWidget()
    ui = Ui_Controls()
    ui.setupUi(Controls)
    Controls.show()
    sys.exit(app.exec_())

