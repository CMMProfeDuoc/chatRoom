import socket

# set up IP and port
host = "localhost"
port = 8080

# creating socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binds the socket with the given IP and port
sock.bind((host, port))

# server is listening and accept maximum one connection at a time
sock.listen(1)
print("The server is running and listening on port : ", port)

# server is accepting the connection from clients
connection, address = sock.accept() # accept return two things -> connection and address of the client.
print("Client", connection, "has joined us recently with address : ", address)

# setting up message from send
message = "Hello from Server to Client"
connection.send(message.encode()) # send message in form of bytes
# close connection at the end
connection.close()