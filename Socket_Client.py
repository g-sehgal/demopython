import  socket

c= socket.socket()

c.connect(('localhost',1234))

name = input("Enter Your Name: ")
c.send(name.encode())
print(c.recv(1024).decode())