import socket
import os, cv2

# Define the server address and port
SERVER_ADDRESS = "0.0.0.0"
SERVER_PORT = 54321

def send_photo(frame):
    try:
        if frame is not None:
            # Initialize a client socket and connect to the server
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

            # Convert the frame to JPEG format
            _, photo_data = cv2.imencode(".jpg", frame)
            file_size = len(photo_data)

            # Send the file size to the server as a 10-character string
            file_size_str = str(file_size).rjust(10, '0')
            client_socket.send(file_size_str.encode())

            # Send the photo data
            client_socket.send(photo_data.tobytes())

            # Close the client socket
            client_socket.close()

            print("Photo sent successfully.")
        else:
            print("No frame captured from the webcam.")
    except Exception as e:
        print(f"Error sending photo: {e}")

'''
def send_photo(photo_path):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

        # Get the file size
        file_size = os.path.getsize(photo_path)
        file_size_str = str(file_size).rjust(10, '0')
        client_socket.send(file_size_str.encode())

        # Send the photo data
        with open(photo_path, "rb") as photo_file:
            while True:
                chunk = photo_file.read(4096)
                if not chunk:
                    break
                client_socket.send(chunk)

        client_socket.close()
        print("Photo sent successfully.")
    except Exception as e:
        print(f"Error sending photo: {e}")
'''
if __name__ == "__main__":
    photo_path = "/home/anton/Pictures/PyFaces/admin.jpg"  # Replace with the path to your photo
    send_photo(photo_path)


'''
import socket

def send_photo_to_server(server_ip, server_port, photo_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    with open(photo_path, 'rb') as file:
        while True:
            photo_data = file.read(2048)
            if not photo_data:
                break
            client_socket.send(photo_data)

    print(f"Sent {photo_path}")

    client_socket.close()
'''
    

'''
import socket

sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender_socket.connect(('127.0.0.1', 54321))

def send_photo(photo_paths):
    with open(photo_paths, 'rb') as photo_file:
        photo_data = photo_file.read(2048)
        while photo_data:
            sender_socket.send(photo_data)
            photo_data = photo_file.read(2048)
        print("sent")
    
    #with open(photo_paths, "rb") as photo_file:
    #    photo_data = photo_file.read()
    #    sender_socket.send(photo_data)
    
def send_photo_2(photo_paths):
    for photo in photo_paths:
        with open(photo, 'rb') as file:
            photo_data = file.read(4096)
            while photo_data:
                sender_socket.send(photo_data)
                photo_data = file.read(4096)
            print(f"sent {photo}")
'''

'''
import socket

server_ip = '0.0.0.0'
server_port = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

def send_photos(photo_paths):
    
    for photo_path in photo_paths:
        with open(photo_path, 'rb') as photo_file:
            photo_data = photo_file.read(1024)
            while photo_data:
                client_socket.send(photo_data)
                photo_data = photo_file.read(1024)

    client_socket.close()

if __name__ == '__main__':
    paths = ['/home/anton/Pictures/PyFaces/admin.jpg']
    send_photos(paths)
'''




'''
import socket

# Receiver's IP and Port
receiver_ip = "0.0.0.0"
receiver_port = 54321

# Function to send a photo
def send_photo(photo_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender_socket:
        sender_socket.connect((receiver_ip, receiver_port))
        with open(photo_path, "rb") as photo_file:
            photo_data = photo_file.read()
            sender_socket.sendall(photo_data)
            message = "Data 1\n Data 2\n"
            sender_socket.send(message.encode("utf-8"))

if __name__ == "__main__":
    photo_path = "/home/anton/Pictures/PyFaces/admin.jpg"  # Replace with the path to your photo
    send_photo(photo_path)

'''




'''

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

def send_message(message, photos):
    client_socket.send(f"MESSAGE: {message}".encode())
    for photo in photos:
        with open(photo, 'rb') as photo_file:
            photo_data = photo_file.read()
            client_socket.send(photo_data)

if __name__ == '__main__':
    photos = ['/home/anton/Pictures/PyFaces/admin.jpg', '/home/anton/Pictures/PyFaces/admin2.png']
    message = "Data 1\n Data 2\n"
    send_message(message, photos)

'''
    
'''

import socket

# Receiver's IP and Port
receiver_ip = "127.0.0.1"
receiver_port = 54321

# Function to send a photo
def send_photo(photo_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender_socket:
        sender_socket.connect((receiver_ip, receiver_port))
        with open(photo_path, "rb") as photo_file:
            photo_data = photo_file.read()
            sender_socket.sendall(photo_data)
            message = "Data 1\n Data 2\n"
            sender_socket.send(message.encode("utf-8"))

if __name__ == "__main__":
    photo_path = "/home/anton/Pictures/PyFaces/admin.jpg"  # Replace with the path to your photo
    send_photo(photo_path)
'''