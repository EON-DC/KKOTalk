# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile_page_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profile_page(object):
    def setupUi(self, profile_page):
        profile_page.setObjectName("profile_page")
        profile_page.resize(414, 292)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(profile_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(profile_page)
        self.widget.setObjectName("widget")
        self.nick_name_label = QtWidgets.QLabel(self.widget)
        self.nick_name_label.setGeometry(QtCore.QRect(140, 80, 111, 61))
        self.nick_name_label.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.nick_name_label.setText("")
        self.nick_name_label.setObjectName("nick_name_label")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(profile_page)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.one_on_one_chatting_btn = QtWidgets.QPushButton(self.widget_2)
        self.one_on_one_chatting_btn.setObjectName("one_on_one_chatting_btn")
        self.horizontalLayout.addWidget(self.one_on_one_chatting_btn)
        self.close_btn = QtWidgets.QPushButton(self.widget_2)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(profile_page)
        QtCore.QMetaObject.connectSlotsByName(profile_page)

    def retranslateUi(self, profile_page):
        _translate = QtCore.QCoreApplication.translate
        profile_page.setWindowTitle(_translate("profile_page", "Form"))
        self.one_on_one_chatting_btn.setText(_translate("profile_page", "1:1 채팅"))
        self.close_btn.setText(_translate("profile_page", "닫기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile_page = QtWidgets.QWidget()
    ui = Ui_profile_page()
    ui.setupUi(profile_page)
    profile_page.show()
    sys.exit(app.exec_())