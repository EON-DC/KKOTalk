import datetime


class Server:
    def __init__(self):
        pass

    def set_config(self, configure):
        print('서버 설정 적용됨')

    def run(self):
        print(f'서버 가동 시작 : {datetime.datetime.now()}')

    def stop(self):
        print(f'서버 종료 시작 : {datetime.datetime.now()}')