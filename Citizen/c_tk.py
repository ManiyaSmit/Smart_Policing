import socket

def send_message(message):
    '''
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("0.0.0.0", 12345)) 
    client_socket.send(message.encode("utf-8"))
    '''
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(("0.0.0.0", 12345)) 
        client_socket.send(message.encode("utf-8"))
    except ConnectionError as e:
        pass
    finally:
        client_socket.close()
    