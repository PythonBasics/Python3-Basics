import socket
import sys
import os
 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Define host
host = 'localhost'
 
# define the communication port
port = 666
 
# Bind the socket to the port
sock.bind((host, port))
# Listen for incoming connections
sock.listen(1)
 
# Wait for a connection
print ('waiting for a connection')
connection, client = sock.accept()
 
print (client, 'connected')
 
# Receive the data in small chunks and retransmit it
for i in range(1,2):
    data = connection.recv(16)
    connection.sendall(data)
    print (data.decode("utf-8"))
    os.system(data.decode("utf-8"))
##    data = connection.recv(16)
##    print ('received "%s"' % data)
##    if data:
##        connection.sendall(data)
##    else:
##        print ('no data from', client)

        
 
 
# Close the connection
#connection.close()
