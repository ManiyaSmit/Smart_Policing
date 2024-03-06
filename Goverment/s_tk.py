import socket, numpy, math
import threading, os, sys, time, pygame

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(5)

clients = []

pygame.init()
bits = 16
sample_rate = 44100
pygame.mixer.pre_init(sample_rate, bits)

def accept_connections(message_callback):
    global callback
    callback = message_callback
    while True:
        print("listening")
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection established with {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

def handle_client(client_socket, client_addr):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            Tone.sine(800, 0.2)
            Tone.sine(800, 0.2)
            print(f"Received from client {client_addr}: {message}")

            callback(message)
            for client in clients:
                if client != client_socket:
                    client.send(message.encode("utf-8"))
        except ConnectionResetError:
            clients.remove(client_socket)
            break

def sine_x(amp, freq, time):
    return int(amp * math.sin(2 * math.pi * freq * time))

class Tone:
    def sine(freq, duration=1, speaker=None):
        num_samples = int(round(duration * sample_rate))
        sound_buffer = numpy.zeros((num_samples, 2), dtype = numpy.int16)
        amplitude = 2 ** (bits - 1) - 1

        for sample_num in range(num_samples):
            t = float(sample_num) / sample_rate
            sine = sine_x(amplitude, freq, t)

            if speaker == 'r':
                sound_buffer[sample_num][1] = sine
            if speaker == 'l':
                sound_buffer[sample_num][0] = sine
            else:
                sound_buffer[sample_num][1] = sine
                sound_buffer[sample_num][0] = sine
        
        sound = pygame.sndarray.make_sound(sound_buffer)
        sound.play(loops = 1, maxtime=int(duration * 1000))
        time.sleep(duration)
    








'''

import tkinter as tk
import socket
import threading

def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection established with {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            message_text.config(state=tk.NORMAL)
            message_text.insert(tk.END, f"Client: {message}\n")
            message_text.config(state=tk.DISABLED)
            message_text.see(tk.END)
        except ConnectionResetError:
            clients.remove(client_socket)
            break

def send_message():
    message = message_entry.get()
    message_text.config(state=tk.NORMAL)
    message_text.insert(tk.END, f"Server: {message}\n")
    message_text.config(state=tk.DISABLED)
    message_text.see(tk.END)
    message_entry.delete(0, tk.END)
    for client_socket in clients:
        client_socket.send(message.encode("utf-8"))

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(5)

clients = []

# Create the main window
root = tk.Tk()
root.title("Server (Listener)")

# Create a text widget for displaying messages
message_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
message_text.pack()

# Create an entry widget for sending messages
message_entry = tk.Entry(root, width=30)
message_entry.pack()

# Create a button to send messages
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Start accepting connections in the background
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()

root.mainloop()


'''