import os
import socket
import tqdm
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Client(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.choose_file_button = QtWidgets.QPushButton('Choose File', self)
        self.choose_file_button.clicked.connect(self.choose_file)

        self.file_name_label = QtWidgets.QLabel(self)

        self.send_file_button = QtWidgets.QPushButton('Send File', self)
        self.send_file_button.clicked.connect(self.send_file)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.choose_file_button)
        vbox.addWidget(self.file_name_label)
        vbox.addWidget(self.send_file_button)

        self.setLayout(vbox)
        self.setWindowTitle('Client')
        self.show()

    def send_file(self):
        host = '127.0.0.1'
        port = 5555
        BUFFER_SIZE = 4096
        SEPARATOR = "<SEPARATOR>"

        # get the file name and size
        file_path = self.file_name_label.text()
        file_name_only = os.path.basename(file_path)
        filesize = os.path.getsize(file_path)

        # create the client socket, connect to the server
        s = socket.socket()
        s.connect((host, port))

        # send the filename and filesize
        s.send(f"{file_name_only}{SEPARATOR}{filesize}".encode())

        # start sending the file
        progress = tqdm.tqdm(range(filesize), f"Sending {file_name_only}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(file_path, "rb") as f:
            while True:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                # we use sendall to assure transmission in 
                # busy networks
                s.sendall(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))

        # close the socket
        s.close()

    def choose_file(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName()[0]
        self.file_name_label.setText(file_path)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ex = Client()
    app.exec_()
