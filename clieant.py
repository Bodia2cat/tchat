import socket
  
sock = socket.socket()
sock.connect(('192.168.0.103', 9090))
sock.send('hello, world!'.encode())
a = "t"
data = sock.recv(1024)
while True:  
	data = sock.recv(1024)
	print(data)
  
	if a == "q":
		exit()
sock.close()