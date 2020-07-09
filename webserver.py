#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) web server."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def accept_incoming_connections():
	"""Sets up handling for incoming clients."""
	while True:
		client, client_address = SERVER.accept()
		print("%s:%s has connected." % client_address)
		Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
	"""Handles a single client connection."""

	while True:
		data = client.recv(1024)
		if len(data) > 0:
			print("Server recv: " + data.decode("utf8"))
			str1 = data.decode("utf8")
			arr1 = str1.split()
			length = len(arr1)

			if arr1[0] == "POST":
				#lay ra user va password
				str2 = arr1[length-1].split('=') #arr1[length-1] la chuoi chua user va password
				str3 = str2[1].split('&')
				user = str3[0]
				password = str2[2]

				#so sanh user va password de dang nhap
				#neu user = admin va password = "admin" => dang nhap thanh cong
				if (user == "admin") and (password == "admin"):
					try:
						client.sendall(bytes("HTTP/1.1 200 OK\r\n", "utf-8"))
						client.sendall(bytes("Content-Type: text/html; charset=utf-8\r\n", "utf-8"))
						client.sendall(bytes("\r\n", "utf-8"))
						file = open ("Member.html", 'rb')
						file_data = file.read(7096)
						client.sendall(file_data)
						client.shutdown(socket.SHUT_RDWR)
					except:
						client.shutdown(socket.SHUT_RDWR)
				else:
					try:
						client.sendall(bytes("HTTP/1.1 200 OK\r\n", "utf-8"))
						client.sendall(bytes("Content-Type: text/html; charset=utf-8\r\n", "utf-8"))
						client.sendall(bytes("\r\n", "utf-8"))
						file = open ("404.html", 'rb')
						file_data = file.read(7096)
						client.sendall(file_data)
						client.shutdown(socket.SHUT_RDWR)
					except:
						client.shutdown(socket.SHUT_RDWR)
			else:
				try:
					client.sendall(bytes("HTTP/1.1 200 OK\r\n", "utf-8"))
					client.sendall(bytes("Content-Type: text/html; charset=utf-8\r\n", "utf-8"))
					client.sendall(bytes("\r\n", "utf-8"))
					file = open ("index.html", 'rb')
					file_data = file.read(7096)
					client.sendall(file_data)
					client.shutdown(socket.SHUT_RDWR)
				except:
					client.shutdown(socket.SHUT_RDWR)


HOST = ''
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
	SERVER.listen(100)
	print("Waiting for connection...")
	ACCEPT_THREAD = Thread(target=accept_incoming_connections)
	
	ACCEPT_THREAD.start()
	ACCEPT_THREAD.join()
	#accept_incoming_connections()
	SERVER.close()
