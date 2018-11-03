import socket
import sys
 
# Create a TCP/IP socket
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Define host
#host="192.168.43.46"
host="127.0.0.1"
 
# define the communication port
port=666
 
# Connect the socket to the port where the server is listening
print(host, port)
server_address = ((host, port))
 
print ("connecting")
 
stream_socket.connect(server_address)
 
 
# Send data
message=bytes("cmd.exe","utf-8")
#message="cmd.exe"
stream_socket.sendall(message)
 
# response
data = stream_socket.recv(10)
print (data)
 
 
print ('socket closed')
stream_socket.close()
