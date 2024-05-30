# Basic server socket in python
import socket


def run_server(server_ip:str):
    # Creating the socket
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket created successfully!")

    # Binding the socket
    port = 12345 
    server.bind((server_ip,port))
    print(f"Socket bound to {server_ip}:{port}")
    
    # Listening for incoming requests
    server.listen(10)
    print("Listening...")
    
    # Accepting connections.
    client,client_address = server.accept()
    print(f"Got connection from:{client_address[0]}")
    
    # Sending and receiving messages
    while True:
        request = client.recv(1024)
        
        if request.lower() == "exit":
            client.close()
            break
        else:
            client.send(request)

    server.close()

run_server("127.0.0.1")