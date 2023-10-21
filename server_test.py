import os
import sys
import socket

# IP = socket.gethostbyname(socket.gethostname())
port = 50001
host = '127.0.0.1'
SIZE = 4096
# FORMAT = "utf-8"
file_command = '!send file'
    
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # sets up socket to be pulled from
server.bind((host,port)) # binds host and port
server.listen() # listens for connections from client

print("Server is listening... ")
conn,addr = server.accept()
print("connected from:" +str(addr))
#recieves data from client 

while True:
    # prompts input from server 
    client_data = conn.recv(SIZE).decode()
    print("Client: "+str(client_data))
     # displays client input   
    if (client_data) == "!send file":
        file_name = conn.recv(SIZE).decode()
        print(file_name)
        file_size = conn.recv(SIZE).decode()
        print(file_size)
        # # recieving filename
        # # filename = conn.recv(SIZE).decode()
        # file = open("text.txt", "rb")
        
        # print ('you are here in the code')
        # print('you are also here in the code')
                
        # conn.send("Filename recieved.".encode())
        # # recieving filedata
        # file_data = conn.recv(SIZE).decode()
        # print(f"[Recieved] File data recieved.")
        # file.read(file_data)
        # conn.send("File data recieved.".encode())
        # file.close()
    if (client_data) == "quit":
        print("client" + str(addr) + " has disconnected, closing..")
        conn.close()
    else:
        message = input(">> ")
        conn.send(message.encode())
