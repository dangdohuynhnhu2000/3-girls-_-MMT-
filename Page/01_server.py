import socket

HOST = "10.0.128.109"
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("Waiting for Client")
conn, addr = s.accept()
try:
    print("Connected by ", addr)
    while True:
        data = conn.recv(1024)
        #conn.sendall(bytes("hello", "utf-8"))
        # if data == "":
        #     print("Detect client close")
        #     break
        if len(data) > 0:
            print("Server recv: " + data.decode("utf8"))
            
            conn.sendall(bytes("HTTP/1.1 200 OK\n", "utf-8"))
            conn.sendall(bytes("Content-Length: 4096\n", "utf-8"))
            conn.sendall(bytes("Content-Type: text/html\n", "utf-8"))
            file = open ("404.html", 'rb')
            file_data = file.read(2000)
            conn.send(file_data)
except KeyboardInterrupt:
    conn.close()
    s.close()
finally:
    conn.close()
    s.close()
