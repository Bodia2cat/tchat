import socket
  
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
  
print('connected:', addr)
  
while True:
    data = conn.recv(1024)

    while True:
    	message = input("message: ")
    	conn.send(message.encode())
  
conn.close()