import socket

#first client

ip = input("Enter server ip: ")
port = input("Port: ")
#first socket
sock = socket.socket()
sock.connect((ip, int(port)))
a = "t"
data = sock.recv(1024)
while True:
	data = sock.recv(1024)
	print(data)
	if a == "q":
		exit()
sock.close()
