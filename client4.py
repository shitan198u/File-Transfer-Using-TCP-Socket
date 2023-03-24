import os
import socket
import tqdm
from tkinter import *
from tkinter import filedialog

def send_file():
    host = '127.0.0.1'
    port = 5555
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"

    # get the file name and size
    file_path = file_name.get()
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

def choose_file():
    file_path = filedialog.askopenfilename()
    file_name.set(file_path)


root = Tk()
root.title("Client")
root.geometry("500x200")

file_name = StringVar()

choose_file_button = Button(root, text="Choose File", command=choose_file)
choose_file_button.pack(pady=10)

file_name_label = Label(root, textvariable=file_name)
file_name_label.pack()

send_file_button = Button(root, text="Send File", command=send_file)
send_file_button.pack(pady=10)

root.mainloop()
