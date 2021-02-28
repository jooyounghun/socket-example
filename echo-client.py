import socket
import pymysql

HOST = '127.0.0.1'
PORT = 9999


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

conn = pymysql.connect(host='localhost', user='root', password='ahfQkd12', db ='study_db', charset='utf8')

curs = conn.cursor()

sql = "select * from test"
curs.execute(sql)

rows = curs.fetchall()

for row in rows:
    client_socket.sendall(row[0])

data = client_socket.recv(1024)
print('Received', repr(data.decode()))

client_socket.close()
