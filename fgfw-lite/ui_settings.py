# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './fgfw-lite/ui\settings.ui'
#
# Created: Sun Nov  9 03:08:39 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(573, 380)
        self.horizontalLayout_5 = QtGui.QHBoxLayout(Settings)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView = QtGui.QTableView(Settings)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.parentRemoveButton = QtGui.QPushButton(Settings)
        self.parentRemoveButton.setObjectName("parentRemoveButton")
        self.horizontalLayout_4.addWidget(self.parentRemoveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.goagentBox = QtGui.QGroupBox(Settings)
        self.goagentBox.setObjectName("goagentBox")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.goagentBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtGui.QLabel(self.goagentBox)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.goagentBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.goagentAPPIDEdit = QtGui.QLineEdit(self.goagentBox)
        self.goagentAPPIDEdit.setObjectName("goagentAPPIDEdit")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.goagentAPPIDEdit)
        self.goagentPassEdit = QtGui.QLineEdit(self.goagentBox)
        self.goagentPassEdit.setObjectName("goagentPassEdit")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.goagentPassEdit)
        self.goagentEnableBox = QtGui.QCheckBox(self.goagentBox)
        self.goagentEnableBox.setObjectName("goagentEnableBox")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.goagentEnableBox)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.goagentSaveButton = QtGui.QPushButton(self.goagentBox)
        self.goagentSaveButton.setObjectName("goagentSaveButton")
        self.horizontalLayout.addWidget(self.goagentSaveButton)
        self.goagentResetButton = QtGui.QPushButton(self.goagentBox)
        self.goagentResetButton.setObjectName("goagentResetButton")
        self.horizontalLayout.addWidget(self.goagentResetButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.goagentBox)
        self.groupBox_2 = QtGui.QGroupBox(Settings)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.ssServerEdit = QtGui.QLineEdit(self.groupBox_2)
        self.ssServerEdit.setObjectName("ssServerEdit")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.ssServerEdit)
        self.ssPortEdit = QtGui.QLineEdit(self.groupBox_2)
        self.ssPortEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.ssPortEdit.setObjectName("ssPortEdit")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.ssPortEdit)
        self.ssMethodBox = QtGui.QComboBox(self.groupBox_2)
        self.ssMethodBox.setObjectName("ssMethodBox")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.ssMethodBox)
        self.ssPassEdit = QtGui.QLineEdit(self.groupBox_2)
        self.ssPassEdit.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.ssPassEdit.setObjectName("ssPassEdit")
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.FieldRole, self.ssPassEdit)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.ssNameEdit = QtGui.QLineEdit(self.groupBox_2)
        self.ssNameEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ssNameEdit.setObjectName("ssNameEdit")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.ssNameEdit)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_8)
        self.ssPriorityEdit = QtGui.QLineEdit(self.groupBox_2)
        self.ssPriorityEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhNoPredictiveText)
        self.ssPriorityEdit.setObjectName("ssPriorityEdit")
        self.formLayout_4.setWidget(5, QtGui.QFormLayout.FieldRole, self.ssPriorityEdit)
        self.verticalLayout_3.addLayout(self.formLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.shadowsocksAddButton = QtGui.QPushButton(self.groupBox_2)
        self.shadowsocksAddButton.setObjectName("shadowsocksAddButton")
        self.horizontalLayout_3.addWidget(self.shadowsocksAddButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "设置", None, QtGui.QApplication.UnicodeUTF8))
        self.parentRemoveButton.setText(QtGui.QApplication.translate("Settings", "移除", None, QtGui.QApplication.UnicodeUTF8))
        self.goagentBox.setTitle(QtGui.QApplication.translate("Settings", "GoAgent", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Settings", "APPID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Settings", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.goagentEnableBox.setText(QtGui.QApplication.translate("Settings", "启用", None, QtGui.QApplication.UnicodeUTF8))
        self.goagentSaveButton.setText(QtGui.QApplication.translate("Settings", "保存", None, QtGui.QApplication.UnicodeUTF8))
        self.goagentResetButton.setText(QtGui.QApplication.translate("Settings", "重置", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Settings", "Shadowsocks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Settings", "服务器地址", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Settings", "服务器端口", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Settings", "　加密方式", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Settings", "　　　密码", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Settings", "服务器名称", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Settings", "　　优先级", None, QtGui.QApplication.UnicodeUTF8))
        self.ssPriorityEdit.setText(QtGui.QApplication.translate("Settings", "99", None, QtGui.QApplication.UnicodeUTF8))
        self.shadowsocksAddButton.setText(QtGui.QApplication.translate("Settings", "添加", None, QtGui.QApplication.UnicodeUTF8))

