# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\DDE_Ocean_Sediments\Rissam\ui\setting_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(607, 369)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_config_file = QtWidgets.QLabel(self.widget_2)
        self.label_config_file.setText("")
        self.label_config_file.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_config_file.setObjectName("label_config_file")
        self.horizontalLayout_3.addWidget(self.label_config_file)
        self.verticalLayout.addWidget(self.widget_2)
        self.category_list_widget = QtWidgets.QListWidget(self.widget)
        self.category_list_widget.setObjectName("category_list_widget")
        self.verticalLayout.addWidget(self.category_list_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.category_input = QtWidgets.QLineEdit(self.widget)
        self.category_input.setObjectName("category_input")
        self.horizontalLayout.addWidget(self.category_input)
        self.color_button = QtWidgets.QToolButton(self.widget)
        self.color_button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.color_button.setText("")
        self.color_button.setObjectName("color_button")
        self.horizontalLayout.addWidget(self.color_button)
        self.add_button = QtWidgets.QPushButton(self.widget)
        self.add_button.setMinimumSize(QtCore.QSize(150, 0))
        self.add_button.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.add_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/书签_bookmark-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_import = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_import.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/传入3_afferent-three.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_import.setIcon(icon1)
        self.pushButton_import.setObjectName("pushButton_import")
        self.horizontalLayout_2.addWidget(self.pushButton_import)
        self.pushButton_export = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_export.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/传出3_efferent-three.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_export.setIcon(icon2)
        self.pushButton_export.setObjectName("pushButton_export")
        self.horizontalLayout_2.addWidget(self.pushButton_export)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cancel_button.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/关闭_close-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(icon3)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.apply_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.apply_button.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/校验_check-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.apply_button.setIcon(icon4)
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout_2.addWidget(self.apply_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Setting"))
        self.label.setText(_translate("Dialog", "Label"))
        self.add_button.setText(_translate("Dialog", "Add new label"))
        self.pushButton_import.setText(_translate("Dialog", "Import"))
        self.pushButton_export.setText(_translate("Dialog", "Export"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.apply_button.setText(_translate("Dialog", "Apply"))
import icons_rc
