import socket
import threading
import os

# Define the server address and port
SERVER_ADDRESS = "0.0.0.0"
SERVER_PORT = 54321

# Define the path to save received photos
SAVE_PATH = "/home/anton/Pictures/received_photos"

# Ensure the save directory exists
os.makedirs(SAVE_PATH, exist_ok=True)

def handle_client(client_socket):
    print(f"Connected: {client_socket.getpeername()}")

    # Receive the file size
    file_size = int(client_socket.recv(10).decode())

    # Receive the photo data
    received_data = b""
    while len(received_data) < file_size:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        received_data += chunk

    # Generate a unique filename for the received photo
    file_path = os.path.join(SAVE_PATH, f"received_{len(os.listdir(SAVE_PATH)) + 1}.jpg")

    # Save the received photo to the specified path
    with open(file_path, "wb") as file:
        file.write(received_data)
        
    img_set(file_path)
    print(f"Received and saved a photo to {file_path}")
    client_socket.close()

def start_server(img_callback):
    global img_set
    img_set = img_callback
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
    server_socket.listen(5)
    print(f"Server listening on {SERVER_ADDRESS}:{SERVER_PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()



'''
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 54321))
server_socket.listen(5)

def start_server(server_ip, server_port):
    print(f"Server listening on {server_ip}:{server_port}")
    c = 0
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        with open(f'/home/anton/Pictures/ppt/{client_address}__{c}.jpg', 'wb') as file:
            c += 1
            while True:
                photo_data = client_socket.recv(2048)
                if not photo_data:
                    break
                file.write(photo_data)


if __name__ == "__main__":
    server_ip = '0.0.0.0'
    server_port = 54321

    server_thread = threading.Thread(target=start_server, args=(server_ip, server_port))
    server_thread.start()
'''




'''
import socket, threading, time

receiver_ip = "127.0.0.1"
receiver_port = 54321

receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_socket.bind((receiver_ip, receiver_port))
receiver_socket.listen(5)

c = 0

def receive_photo():
    global c
    while True:
        print("listening...")
        conn, addr = receiver_socket.accept()
        print(f"Connected : {addr}")
        save_path = f"/home/anton/Pictures/PyFaces/received_img_{c}.jpg"
        c += 1
        with open(save_path, "wb") as photo_file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                photo_file.write(data)
        print(f"Photo received and saved as {save_path}")

def receive_photo_2():
    client_socket, client_addr = receiver_socket.accept()
    print(f"Accepted connection from : {client_addr}")
    c = 0
    while True:
        c += 1
        photo_data = client_socket.recv(1024)
        if not photo_data:
            break
        with open(f'/home/anton/Pictures/PyFaces/recv_img_{c}.jpg', 'wb') as file:
            file.write(photo_data)
        print("recieved")

def receive_photo_3():
    while True:
        client_socket, client_addr = receiver_socket.accept()
        print(f"Accepted connection from : {client_socket}")
        photo_data = client_socket.recv(1024)
        with open(f'/home/anton/Pictures/   RECEIVED/{client_addr}.jpg', 'wb') as file:
            while photo_data:
                file.write(photo_data)
                photo_data = client_socket.recv(1024)
        print("received")

def receive_photo_4():
    while True:
        client_socket, client_addr = receiver_socket.accept()
        print(f"Accepted connection from : {client_addr}")
        with open(f'/home/anton/Pictures/RECEIVED/{client_addr}.jpg', 'wb') as file:
            img_chunk = client_socket.recv(2048)
            while img_chunk:
                file.write(img_chunk)
                img_chunk = client_socket.recv(2048)
        print("Recieved")

if __name__ == "__main__": 
    client_thread = threading.Thread(target=receive_photo_4, args=())
    client_thread.start()
'''





'''
import socket
import threading
import os

server_ip = '0.0.0.0' 
server_port = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)

print(f"Server is listening on {server_ip}:{server_port}")

clients = []

def handle_client(client_socket):
    while True:
        photo_data = client_socket.recv(1024)
        if not photo_data:
            break
        with open(f"/home/anton/Pictures/PyFaces/received_photo.jpg", "wb") as photo_file:
            photo_file.write(photo_data)

    print(f"Received and saved photo from {client_socket.getpeername()}")
    client_socket.close()

def accept_clients():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        
        clients.append(client_socket)
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    accept_thread = threading.Thread(target=accept_clients)
    accept_thread.start()
'''


'''
import socket

# Receiver's IP and Port
receiver_ip = "0.0.0.0"
receiver_port = 54321

# Function to receive and save a photo
def receive_photo(save_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receiver_socket:
        receiver_socket.bind((receiver_ip, receiver_port))
        receiver_socket.listen()
        conn, addr = receiver_socket.accept()
        with open(save_path, "wb") as photo_file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                photo_file.write(data)
        message = receiver_socket.recv(1024).decode("utf-8")
        print(message)

if __name__ == "__main__":
    save_path = "/home/anton/Pictures/PyFaces/RECIEVED.jpg"  # Set the path to save the received photo
    receive_photo(save_path)
    print(f"Photo received and saved as {save_path}")
'''

'''
import socket, threading, time, os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(5)

clients = []
clients_addr = []

def accept_connection():
    while True:
        print("listening...")
        client_socket, client_addr = server_socket.accept()
        clients.append(client_socket)
        clients_addr.append(client_addr)
        print(f"Connection established with : {client_addr}")
        client_thread = threading.Thread(target = handle_client, args = (client_socket, client_addr,))
        client_thread.start()

def handle_client(client_socket, client_addr):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            if data.startswith(b"MESSAGE:"):
                message = data[len(b"MESSAGE:"):]
                print(f"Recieved message from {client_addr} : {message}")
            else:
                photo_name = f"photo_{time.time()}.jpg"
                with open(os.path.join('/home/anton/Pictures/PyFaces/', photo_name), "wb") as photo_file:
                    photo_file.write(data)
                    print(f"Recieved photo from {client_addr} : {message}")
        except ConnectionResetError:
            clients.remove(client_socket)
            clients_addr.remove(client_addr)
            break
    
if __name__ == '__main__':
    accept_connection()

    '''

'''

import socket

# Receiver's IP and Port
receiver_ip = "127.0.0.1"
receiver_port = 54321

# Function to receive and save a photo
def receive_photo(save_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receiver_socket:
        receiver_socket.bind((receiver_ip, receiver_port))
        receiver_socket.listen()
        conn, addr = receiver_socket.accept()
        with open(save_path, "wb") as photo_file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                photo_file.write(data)
        message = receiver_socket.recv(1024).decode("utf-8")
        print(message)

if __name__ == "__main__":
    save_path = "/home/anton/Pictures/PyFaces/RECIEVED.jpg"  # Set the path to save the received photo
    receive_photo(save_path)
    print(f"Photo received and saved as {save_path}")

    '''