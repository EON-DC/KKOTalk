import os
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

from Code.domain.class_user import User
from Code.network.class_worker_thread import WorkerServerThread
from Code.network.server_ui.ui_server_controller_widget import Ui_server_controller


class ServerControllerWidget(QtWidgets.QWidget, Ui_server_controller):
    ENCODED_DOT = bytes('.', 'utf-8')
    ENCODED_PASS = bytes('pass', 'utf-8')
    LOG_PATH = """C:\\Users\\KDT107\\Desktop\\KKOTalk\\log.txt"""

    @staticmethod
    def check_netstat_via_cmd():
        os.system("""C:\\Users\\KDT107\\Desktop\\KKOTalk\\Code\\network\\server_logger.bat""")

    def __init__(self, server_obj, db_connector):
        super().__init__()
        self.setupUi(self)
        self.server = server_obj
        self.db_conn = db_connector
        self.check_timer = None
        self.set_initial_label()
        self.set_btn_trigger()
        self.set_timer_to_check_server_status()

    def set_timer_to_check_server_status(self):
        self.check_timer = QtCore.QTimer(self)
        self.check_timer.setInterval(1000)
        self.check_timer.timeout.connect(lambda: self.assert_server_status())
        self.check_timer.start()

    def get_log_line_count(self):
        with open(self.LOG_PATH, "r", encoding="utf-8") as file:
            return len(file.read().split())

    def is_server_running(self):
        total_line_count = self.get_log_line_count()
        self.check_netstat_via_cmd()  # 서버 켜지있으면 한줄 더 늘어남
        now_log_line_count = self.get_log_line_count()
        if now_log_line_count != total_line_count:  # 서버가 켜저있는 경우
            return True
        else:
            return False

    def assert_server_status(self):
        if self.is_server_running() is True:
            self.label_server_status.setText("🟢 가동중")
        else:
            self.label_server_status.setText("🔴 종료됨")
        # self.label_server_status.setText("🟠 시작중")

    def set_initial_label(self):
        # todo check serve status logic
        self.label_server_status.setText("🔴 종료됨")

    def set_btn_trigger(self):
        self.btn_run.clicked.connect(lambda state: self.server_run())
        self.btn_stop.clicked.connect(lambda state: self.server_stop())

    def server_run(self):
        self.server.start()

    def server_stop(self):
        self.server.stop()
        temp_time = QtCore.QTimer(self)
        temp_time.singleShot(1000, lambda: self.task_server_kill())

    def task_server_kill(self):
        last_line = None
        with open(self.LOG_PATH, "r", encoding="utf-8") as file:
            last_line = file.read().split('\n')[-2]
        if last_line is not None:
            now_pid = last_line.split('\t')[-1]
            os.system(f"taskkill /pid {now_pid}")


    def listening(self):
        while True:
            msg = self.server.recv(1024).decode("utf-8")
            if msg == '/assert_username':
                self.server.send(self.ENCODED_DOT)
                response = self.server.recv(1024).decode("utf-8")
                if self.db_conn.assert_same_join_id(response) is True:
                    self.server.send(self.ENCODED_PASS)
                else:
                    self.server.send('.'.encode())
            elif msg == '/join_user':
                self.server.send(self.ENCODED_DOT)
                response = self.server.recv(1024).decode("utf-8")
                if self.join_access(response) is True:
                    self.server.send('pass'.encode(encoding='utf-8'))
                else:
                    self.server.send(self.ENCODED_PASS)
            elif msg == '/login':
                self.server.send(self.ENCODED_DOT)
                response = self.server.recv(1024).decode("utf-8")
                if self.join_access(response) is True:
                    self.server.send(self.ENCODED_PASS)
                else:
                    self.server.send(self.ENCODED_DOT)

    def assert_same_join_id(self, input_username):
        return self.db_conn.assert_same_login_id(input_username)

    def join_access(self, join_user_json_str: str):
        join_user_obj = self.decoder.decode(join_user_json_str)
        join_user_obj: User
        if self.db_conn.insert_user(join_user_obj) is not False:
            print(f"유저 {join_user_obj.nickname} 가입 성공")
            return True
        else:
            return False

    def login_access(self, login_message: str):
        username, pw = login_message.split('%')
        if self.db_conn.user_log_in(username, pw):
            print(f"유저 {username} 로그인 성공")
            return True
        else:
            return False
