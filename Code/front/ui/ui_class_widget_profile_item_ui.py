# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_profile_item_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profile_widget(object):
    def setupUi(self, profile_widget):
        profile_widget.setObjectName("profile_widget")
        profile_widget.resize(459, 80)
        profile_widget.setMinimumSize(QtCore.QSize(459, 80))
        profile_widget.setMaximumSize(QtCore.QSize(459, 80))
        profile_widget.setStyleSheet("#out_widget {\n"
"    background-color: #FFFFFF;\n"
"    color: #331D2C;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: #1D5D9B;\n"
"    border-radius: 5px;\n"
"}\n"
"#out_widget:hover{\n"
"    background-color: #E6FFFD;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"    color: #1D5D9B;\n"
"    font: bold 16pt \"나눔고딕\";\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(profile_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.out_widget = QtWidgets.QWidget(profile_widget)
        self.out_widget.setObjectName("out_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.out_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.profile = QtWidgets.QWidget(self.out_widget)
        self.profile.setStyleSheet("")
        self.profile.setObjectName("profile")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.profile)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.profile_name_label = QtWidgets.QLabel(self.profile)
        self.profile_name_label.setObjectName("profile_name_label")
        self.horizontalLayout_2.addWidget(self.profile_name_label)
        self.horizontalLayout.addWidget(self.profile)
        self.verticalLayout.addWidget(self.out_widget)

        self.retranslateUi(profile_widget)
        QtCore.QMetaObject.connectSlotsByName(profile_widget)

    def retranslateUi(self, profile_widget):
        _translate = QtCore.QCoreApplication.translate
        profile_widget.setWindowTitle(_translate("profile_widget", "Form"))
        self.profile_name_label.setText(_translate("profile_widget", "닉네임"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile_widget = QtWidgets.QWidget()
    ui = Ui_profile_widget()
    ui.setupUi(profile_widget)
    profile_widget.show()
    sys.exit(app.exec_())
