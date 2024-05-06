import socket

s= socket.socket()
print("Socket Connected")

s.bind(('localhost', 1234))
s.listen(3)

while True:
    c, addr = s.accept()
    name= c.recv(1024).decode()
    print("Got connection from", addr, name)
    c.send("Thank you for connecting".encode())
    c.close()