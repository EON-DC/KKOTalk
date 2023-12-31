# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_talk_room_invite_user_list_in_chat_room.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_make_talk_room_widget(object):
    def setupUi(self, make_talk_room_widget):
        make_talk_room_widget.setObjectName("make_talk_room_widget")
        make_talk_room_widget.resize(542, 477)
        make_talk_room_widget.setStyleSheet("#widget {\n"
"    background-color: #75C2F6;\n"
"    color: #1D5D9B;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"    color: #1D5D9B;\n"
"    font: bold 16pt \"나눔고딕\";\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#F4D160;\n"
"    color: #1D5D9B;\n"
"    font: bold 12pt \"나눔고딕\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#FFFF9D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:#FEF5AC;\n"
"}\n"
"\n"
"\n"
"#label_title{\n"
"    font: bold 20pt \"나눔고딕\";\n"
"    color: #F4D160;\n"
"}\n"
"\n"
"#frame_title{\n"
"    background-color: #1D5D9B;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: #1D5D9B;\n"
"    font: bold 12pt \"나눔고딕\";\n"
"}\n"
"")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(make_talk_room_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(make_talk_room_widget)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_most_out = QtWidgets.QWidget(self.widget)
        self.widget_most_out.setObjectName("widget_most_out")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_most_out)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_title = QtWidgets.QFrame(self.widget_most_out)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setMinimumSize(QtCore.QSize(0, 0))
        self.label_title.setWordWrap(False)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_4.addWidget(self.label_title)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btn_flist_close = QtWidgets.QPushButton(self.frame_title)
        self.btn_flist_close.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_flist_close.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_flist_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_flist_close.setIcon(icon)
        self.btn_flist_close.setObjectName("btn_flist_close")
        self.horizontalLayout_4.addWidget(self.btn_flist_close)
        self.verticalLayout_3.addWidget(self.frame_title)
        self.scrollArea = QtWidgets.QScrollArea(self.widget_most_out)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.widget_3 = QtWidgets.QWidget()
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 522, 279))
        self.widget_3.setObjectName("widget_3")
        self.layout = QtWidgets.QVBoxLayout(self.widget_3)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.setObjectName("layout")
        self.invite_member_choice = QtWidgets.QWidget(self.widget_3)
        self.invite_member_choice.setObjectName("invite_member_choice")
        self.invite_member_choice_layout = QtWidgets.QVBoxLayout(self.invite_member_choice)
        self.invite_member_choice_layout.setObjectName("invite_member_choice_layout")
        self.layout.addWidget(self.invite_member_choice)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 291, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.layout.addWidget(self.widget_2)
        self.scrollArea.setWidget(self.widget_3)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.widget_footer = QtWidgets.QWidget(self.widget_most_out)
        self.widget_footer.setObjectName("widget_footer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_footer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.widget_footer)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.frame)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_invite_user_nickname_list = QtWidgets.QLabel(self.widget_6)
        self.label_invite_user_nickname_list.setObjectName("label_invite_user_nickname_list")
        self.horizontalLayout_6.addWidget(self.label_invite_user_nickname_list)
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.label_user_count = QtWidgets.QLabel(self.widget_6)
        self.label_user_count.setMinimumSize(QtCore.QSize(50, 0))
        self.label_user_count.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_user_count.setObjectName("label_user_count")
        self.horizontalLayout_6.addWidget(self.label_user_count)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.frame_2 = QtWidgets.QFrame(self.widget_5)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.decision_btn = QtWidgets.QPushButton(self.frame_2)
        self.decision_btn.setObjectName("decision_btn")
        self.horizontalLayout_3.addWidget(self.decision_btn)
        self.close_btn = QtWidgets.QPushButton(self.frame_2)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_3.addWidget(self.close_btn)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.widget_footer)
        self.horizontalLayout_2.addWidget(self.widget_most_out)
        self.verticalLayout_4.addWidget(self.widget)

        self.retranslateUi(make_talk_room_widget)
        QtCore.QMetaObject.connectSlotsByName(make_talk_room_widget)

    def retranslateUi(self, make_talk_room_widget):
        _translate = QtCore.QCoreApplication.translate
        make_talk_room_widget.setWindowTitle(_translate("make_talk_room_widget", "Form"))
        self.label_title.setText(_translate("make_talk_room_widget", "초대목록"))
        self.label_invite_user_nickname_list.setText(_translate("make_talk_room_widget", "닉네임 리스트"))
        self.label_2.setText(_translate("make_talk_room_widget", "선택:"))
        self.label_user_count.setText(_translate("make_talk_room_widget", "0명"))
        self.decision_btn.setText(_translate("make_talk_room_widget", "확인"))
        self.close_btn.setText(_translate("make_talk_room_widget", "취소"))
from Code.front.ui import my_qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    make_talk_room_widget = QtWidgets.QWidget()
    ui = Ui_make_talk_room_widget()
    ui.setupUi(make_talk_room_widget)
    make_talk_room_widget.show()
    sys.exit(app.exec_())
