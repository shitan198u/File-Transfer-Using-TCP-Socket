TCP Socket File Transfer using Python
=====================================

This repository contains a simple file transfer application using TCP sockets in Python. It consists of a server and a client that allow you to send files from the client to the server.

Prerequisites
-------------

To run this application, you need to have the following installed:

* Python (version 3.7 or higher)
* pipenv (for managing the virtual environment)

Installation
------------

1. Clone the repository to your local machine:
    
    ```shell
    git clone https://github.com/shitan198u/File-Transfer-Using-TCP-Socket.git
    ```
    
2. Navigate to the project directory:
    
    ```shell
    cd File-Transfer-Using-TCP-Socket
    ```
3. Install pipenv if you haven't already:
    
    ```shell
   pip install pipenv
    ```

4. Create a virtual environment and install the dependencies:
    
    ```shell
    pipenv install
    ```
    
    This will automatically create a virtual environment and install the required dependencies (`pyqt5` and `tqdm`) specified in the `Pipfile`.
    
5. Activate the virtual environment:
    
    ```shell
    pipenv shell
    ```
    

Usage
-----

### Server

The server should be run first before starting the client.

To start the server, run the following command:

```shell
python server.py
```

The server will start listening for incoming connections on `0.0.0.0:5555`. When a client connects and sends a file, it will be received and saved in the `./REC` directory.

### Client

To start the client application, run the following command:

```shell
python client.py
```

The client application will open a graphical user interface (GUI) window. Follow these steps to send a file:

1. Click on the "Choose File" button to select the file you want to send.
2. The selected file's name will be displayed below the button.
3. Click on the "Send File" button to start sending the file to the server.

The progress of the file transfer will be displayed in the console, showing the transmission speed and progress bar.

Example
-------

Here is an example workflow demonstrating how to use the file transfer application:

1. Start the server:
    
    ```shell
    python server.py
    ```
    
    The server will start listening for incoming connections.
    
2. Start the client:
    
    ```shell
    python client.py
    ```
    
    The client application window will open.
    
3. Select a file to send:
    
    * Click on the "Choose File" button.
    * Browse your filesystem and select the file you want to send.
    * The selected file's name will be displayed below the button.
4. Send the file:
    
    * Click on the "Send File" button.
    * The file transfer progress will be displayed in the console.
5. Verify the file transfer:
    
    * On the server-side, the received file will be saved in the `./REC` directory.

Note: Make sure to start the server before running the client and ensure that both the server and client are running on the same network.

Contributing
------------

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or a pull request.

License
-------

This project is licensed under the [MIT License](LICENSE).

Acknowledgements
----------------

This project was inspired by the need for a simple file transfer mechanism using TCP sockets in Python. Special thanks to the developers of PyQt5 and tqdm for their excellent libraries.
