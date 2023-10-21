import os
import sys
import socket


# IP = socket.gethostbyname(socket.gethostname())
port = 50001
host = '127.0.0.1'
SIZE = 1024
FORMAT = "utf-8"



client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # setup of new client object
client.connect((host,port)) # connect to server 
print("Connecting to server... please wait... ")
message = input(">> ") # user message input prompt 
# print("Welcome user. Type quit to exit program.")

    
while True:
    server_data = client.recv(SIZE).decode()
    print("Server: "+str(server_data)) 
    if message == '!send file':
        file = open("sats_FINAL.png",'rb')
        file_size = os.path.getsize("sats_FINAL.png")
        
        client.send("recieved_image.png".encode())
        client.send(str(file_size).encode())
        
        data = file.read()
        client.sendall(data)
        client.send(b"<END>")
        
        file.close() 
    if message == "quit":
        client.close() 
    else:  
        message = input(">> ")
        client.send(message.encode()) 
       

