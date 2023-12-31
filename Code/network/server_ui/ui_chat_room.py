# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype_chat_room.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_prototype(object):
    def setupUi(self, prototype):
        prototype.setObjectName("prototype")
        prototype.resize(674, 638)
        self.verticalLayout = QtWidgets.QVBoxLayout(prototype)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(prototype)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.widget_7)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.btn_init = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_init.sizePolicy().hasHeightForWidth())
        self.btn_init.setSizePolicy(sizePolicy)
        self.btn_init.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_init.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_init.setObjectName("btn_init")
        self.horizontalLayout_4.addWidget(self.btn_init)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.text_edit_chat_room = QtWidgets.QPlainTextEdit(self.widget)
        self.text_edit_chat_room.setReadOnly(True)
        self.text_edit_chat_room.setObjectName("text_edit_chat_room")
        self.verticalLayout_2.addWidget(self.text_edit_chat_room)
        self.verticalLayout.addWidget(self.widget)
        self.widget_6 = QtWidgets.QWidget(prototype)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.widget_8)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.line_edit_for_join_id = QtWidgets.QLineEdit(self.widget_8)
        self.line_edit_for_join_id.setObjectName("line_edit_for_join_id")
        self.horizontalLayout_7.addWidget(self.line_edit_for_join_id)
        self.btn_check_same_id = QtWidgets.QPushButton(self.widget_8)
        self.btn_check_same_id.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_check_same_id.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_check_same_id.setObjectName("btn_check_same_id")
        self.horizontalLayout_7.addWidget(self.btn_check_same_id)
        self.label_6 = QtWidgets.QLabel(self.widget_8)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.line_edit_for_join_pw = QtWidgets.QLineEdit(self.widget_8)
        self.line_edit_for_join_pw.setObjectName("line_edit_for_join_pw")
        self.horizontalLayout_7.addWidget(self.line_edit_for_join_pw)
        self.label_4 = QtWidgets.QLabel(self.widget_8)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.line_edit_for_join_nick = QtWidgets.QLineEdit(self.widget_8)
        self.line_edit_for_join_nick.setObjectName("line_edit_for_join_nick")
        self.horizontalLayout_7.addWidget(self.line_edit_for_join_nick)
        self.btn_join = QtWidgets.QPushButton(self.widget_8)
        self.btn_join.setObjectName("btn_join")
        self.horizontalLayout_7.addWidget(self.btn_join)
        self.horizontalLayout_5.addWidget(self.widget_8)
        self.verticalLayout.addWidget(self.widget_6)
        self.widget_3 = QtWidgets.QWidget(prototype)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.line_edit_for_login_id = QtWidgets.QLineEdit(self.widget_5)
        self.line_edit_for_login_id.setObjectName("line_edit_for_login_id")
        self.horizontalLayout_3.addWidget(self.line_edit_for_login_id)
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.line_edit_for_login_pw = QtWidgets.QLineEdit(self.widget_5)
        self.line_edit_for_login_pw.setObjectName("line_edit_for_login_pw")
        self.horizontalLayout_3.addWidget(self.line_edit_for_login_pw)
        self.btn_login = QtWidgets.QPushButton(self.widget_5)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_3.addWidget(self.btn_login)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(prototype)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(100, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.line_edit_nickname_for_chat = QtWidgets.QLineEdit(self.widget_4)
        self.line_edit_nickname_for_chat.setObjectName("line_edit_nickname_for_chat")
        self.verticalLayout_3.addWidget(self.line_edit_nickname_for_chat)
        self.horizontalLayout.addWidget(self.widget_4)
        self.text_edit_for_send_chat = QtWidgets.QPlainTextEdit(self.widget_2)
        self.text_edit_for_send_chat.setObjectName("text_edit_for_send_chat")
        self.horizontalLayout.addWidget(self.text_edit_for_send_chat)
        self.btn_send_message = QtWidgets.QPushButton(self.widget_2)
        self.btn_send_message.setMinimumSize(QtCore.QSize(100, 80))
        self.btn_send_message.setObjectName("btn_send_message")
        self.horizontalLayout.addWidget(self.btn_send_message)
        self.btn_transfer_file = QtWidgets.QPushButton(self.widget_2)
        self.btn_transfer_file.setMinimumSize(QtCore.QSize(100, 80))
        self.btn_transfer_file.setObjectName("btn_transfer_file")
        self.horizontalLayout.addWidget(self.btn_transfer_file)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(prototype)
        QtCore.QMetaObject.connectSlotsByName(prototype)

    def retranslateUi(self, prototype):
        _translate = QtCore.QCoreApplication.translate
        prototype.setWindowTitle(_translate("prototype", "Form"))
        self.label_10.setText(_translate("prototype", "전체 채팅방"))
        self.btn_init.setText(_translate("prototype", "텍스트 초기화"))
        self.label_7.setText(_translate("prototype", "회원가입\n"
"테스트용"))
        self.label_5.setText(_translate("prototype", "아이디"))
        self.btn_check_same_id.setText(_translate("prototype", "중복쳌"))
        self.label_6.setText(_translate("prototype", "패스워드"))
        self.label_4.setText(_translate("prototype", "닉네임"))
        self.btn_join.setText(_translate("prototype", "회원가입"))
        self.label_9.setText(_translate("prototype", "로그인\n"
"테스트용"))
        self.label.setText(_translate("prototype", "아이디"))
        self.label_2.setText(_translate("prototype", "패스워드"))
        self.btn_login.setText(_translate("prototype", "로그인"))
        self.label_8.setText(_translate("prototype", "채팅\n"
"테스트용"))
        self.label_3.setText(_translate("prototype", "닉네임"))
        self.text_edit_for_send_chat.setPlaceholderText(_translate("prototype", "채팅 입력 공간"))
        self.btn_send_message.setText(_translate("prototype", "전송하기"))
        self.btn_transfer_file.setText(_translate("prototype", "파일\n"
"전송하기"))
