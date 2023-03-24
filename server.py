import os
import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5555
BUFFER_SIZE = 4096  # 4KB buffer size
SEPARATOR = "<SEPARATOR>"

def receive_file(conn, address):
    if not os.path.exists("REC"):
        os.makedirs("REC")
    received = conn.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    file_path = os.path.join("REC", filename)
    with open(file_path, "wb") as f:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
    conn.close()
    print(f"File received from {address[0]}:{address[1]} saved as {file_path}")


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    while True:
        conn, address = s.accept()
        print(f"[+] {address[0]}:{address[1]} is connected.")
        receive_file(conn, address)

start_server()
