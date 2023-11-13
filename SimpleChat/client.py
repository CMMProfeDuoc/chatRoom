import socket  # importing socket library

# setting up host and port same as used on server side
host = "localhost"
port = 8080

# create object of socket on client side
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server by providing same host and port that has been used on server side.
sock.connect((host, port))

# receive message from server
message = sock.recv(1024).decode()

# keep receiving message from server. in loop
while message:
    # display the message received from server side.
    print("Message : ", message)
    message = sock.recv(1024).decode()

# close client at the end
sock.close()