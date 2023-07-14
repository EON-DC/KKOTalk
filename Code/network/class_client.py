import socket
from threading import *
from Code.domain.class_user import User
from Common.class_json import KKODecoder


class ClientApp:
    HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 1024
    FORMAT = "utf-8"
    HEADER_LENGTH = 30


    assert_username = "assert_username"
    join_user = "join_user"
    login = "login"
    enter_square = "enter_square"
    all_user_list = "all_user_list"
    user_talk_room_list = "user_talk_room_list"
    invite_user_talk_room = "invite_user_talk_room"
    send_msg_c_room = "send_msg_c_room"
    send_alarm_c_room = "send_alarm_c_room"

    HEADER_LIST = {
        assert_username: assert_username.encode(FORMAT),
        join_user: join_user.encode(FORMAT),
        login: login.encode(FORMAT),
        send_msg_c_room: send_msg_c_room.encode(FORMAT),
        send_alarm_c_room: send_alarm_c_room.encode(FORMAT),
    }

    def __init__(self):
        # 서버 소켓 설정
        self.client_socket = None
        self.config = None
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        # self.client_socket.setblocking(False)
        self.username = None
        self.user_id = None
        self.user_pw = None
        self.user_nickname = None
        self.receive_thread = Thread(target=self.receive_message)
        self.receive_thread.start()
        self.client_widget = None
        self.decoder = KKODecoder()

        # client function =================================

    def set_widget(self, widget_):
        self.client_widget = widget_

    def send_join_id_for_assert_same_username(self, input_username: str):
        data_msg = f"{input_username:<{self.BUFFER-self.HEADER_LENGTH}}".encode(self.FORMAT)
        data_msg_length = len(data_msg)
        request_msg = self.assert_username
        header_msg = f"{request_msg:<{self.HEADER_LENGTH}}".encode(self.FORMAT)
        self.client_socket.send(header_msg + data_msg)  # 헤더를 붙이고 보내는 동작(?)


    def send_join_id_and_pw_for_join_access(self, join_username, join_pw, join_nickname):
        join_user = User(None, join_username, join_pw, join_nickname)
        user_json_str = join_user.toJSON()
        request_msg = self.join_user
        result = self.fixed_volume(request_msg, user_json_str)
        self.client_socket.send(result)

    def send_login_id_and_pw_for_login_access(self, login_username, login_pw):
        # 로그인 파일이 있다고 가정하고 제작
        login_user = User(None, login_username, login_pw, None)
        login_user_str = login_user.toJSON()
        request_msg = self.login
        result = self.fixed_volume(request_msg, login_user_str)
        self.client_socket.send(result)  # 응답 받기

    # 로그인시 가져와야하는 정보들을 한번에 묶을수 있을까? 헤더 그리고 반환값이 달라서 문제임
    def send_enter_square(self):
        user_object = User(self.user_id, self.username, self.user_pw, self.user_nickname)
        user_object_str = user_object.toJSON()
        request_msg = self.enter_square
        result = self.fixed_volume(request_msg, user_object_str)
        self.client_socket.send(result)

    def send_all_user_list(self):
        user_object = User(self.user_id, self.username, self.user_pw, self.user_nickname)
        user_object_str = user_object.toJSON()
        request_msg = self.all_user_list
        result = self.fixed_volume(request_msg, user_object_str)
        self.client_socket.send(result)

    def send_user_talk_room_list(self):
        user_object = User(self.user_id, self.username, self.user_pw, self.user_nickname)
        user_object_str = user_object.toJSON()
        request_msg = self.user_talk_room_list
        result = self.fixed_volume(request_msg, user_object_str)
        self.client_socket.send(result)

    # 크기 고정으로 만들어 주는 함수
    def fixed_volume(self, header, data):
        header_msg = f"{header:<{self.HEADER_LENGTH}}".encode(self.FORMAT)
        data_msg = f"{data:<{self.BUFFER - self.HEADER_LENGTH}}".encode(self.FORMAT)
        return header_msg + data_msg

    def send_message_to_chat_room(self):
        # todo: send 메시지
        pass

    def send_file_to_chat_room(self):
        # todo: send 메시지
        pass

    def receive_message(self):
        while True:
            # self.return_result = self.client_socket.recv(self.BUFFER).decode(self.FORMAT)
            return_result = self.client_socket.recv(self.BUFFER).decode(self.FORMAT)
            response_header = return_result[:self.HEADER_LENGTH].strip()
            print(response_header)
            response_data = return_result[self.HEADER_LENGTH:].strip()
            # 아이디 중복 확인 결과
            if response_header == self.assert_username:
                if response_data == 'pass':
                    self.client_widget.assert_same_id_signal.emit(True)
                elif response_data == '.':
                    self.client_widget.assert_same_id_signal.emit(False)
            # 회원 가입 중복 확인 결과
            elif response_header == self.join_user:
                if response_data == 'pass':
                    self.client_widget.sign_up_signal.emit(True)
                elif response_data == '.':
                    self.client_widget.sign_up_signal.emit(False)
            # 로그인 신청 확인 결과, 로그인한 유저정보 저장?
            elif response_header == self.login:
                if response_data == '.':
                    self.client_widget.log_in_signal.emit(False)
                else:
                    object_data = self.decoder.decode_any(response_data)
                    self.username = object_data.username
                    self.user_id = object_data.user_id
                    self.user_pw = object_data.password
                    self.user_nickname = object_data.nickname
                    self.client_widget.log_in_signal.emit(True)
            # 초기 단톡방 입장 반환
            elif response_header == self.enter_square:
                if response_data == 'pass':
                    self.client_widget.enter_square_signal.emit(True)
            # 본인 제외 모든 유저 정보
            elif response_header == self.all_user_list:
                if response_data == '.':
                    print('오류?')
                else:
                    self.client_widget.all_user_list_signal.emit(response_data)
            # 채팅방 리스트 정보
            elif response_header == self.user_talk_room_list:
                self.client_widget.user_talk_room_signal.emit(response_data)

