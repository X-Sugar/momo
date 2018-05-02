import socket

sk = socket.socket()

sk.bind(('127.0.0.1',8888))
sk.listen(5)

conn,addr = sk.accept()

print(conn)
print(addr)

acccep_data = conn.recv(1024)
acccep_data2 = str(acccep_data,encoding='utf8')

print(acccep_data2,str(addr[1]))

send_data = input('请输入发送的内容：')
conn.sendall(bytes(send_data,encoding='utf8'))
conn.close()