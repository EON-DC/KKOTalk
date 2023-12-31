import sys
from datetime import datetime

from PyQt5.QtWidgets import QApplication

from Code.domain.class_db_connector import DBConnector
from Code.domain.class_talk_room import TalkRoom
from Code.network.class_server import Server
from Code.network.class_server_controller_widget import ServerControllerWidget
from Common.common_module import *





if __name__ == '__main__':
    app = QApplication(sys.argv)
    db_conn = DBConnector(test_option=True)
    # db_conn.create_tables()
    # square_talkroom = TalkRoom(1, 'square', f'{datetime.now()}')
    # db_conn.insert_talk_room(square_talkroom)
    server = Server(db_conn)
    server.start()
    # proto_widget = ServerControllerWidget(server, db_conn)
    # proto_widget.show()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    sys.exit(app.exec_())