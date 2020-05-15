import socket
  
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

sock2 = socket.socket()
print("Server is start!")
sock2.bind(('', 8080))
sock2.listen(1)
conn2, addr2 = sock2.accept()
print('connected:', addr)
while True:
    data = conn.recv(1024)

    while True:
    	print('connected: ', addr2)
    	message = input("message: ")
    	conn.send(message.encode())
    	conn2.send(message.encode())
  		
conn.close()