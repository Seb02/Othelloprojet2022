import socket
import sys
import json
import socket

class othelloIA: #initialsation du socket 
	def __init__(self, ipbut = "localhost", port = 2048 ): #port 2048 : utilisé en local quand l'ordi se comporte comme serveur
		self.port = port
		self.ipbut = ipbut
		 
		self.s = socket.socket()  
		serverAddress = (self.ipbut, 3000) #port 3000 : utilisé pour atteindre le serveur de gestion des jeux
		self.s.connect(serverAddress)
		#self.receptionsocket = socket.socket()
		
		
		
		
		
	
	def inscription(self):

		renseignements = json.dumps({
   		"request": "subscribe",
   		"port": self.port,
   		"name": "IA2003420342",
   		"matricules": ["20034", "20342"]
		}) #json.dumps() function converts a Python object into a json string.
		self.s.send(renseignements.encode('utf8'))
		self.PingPong()
	def PingPong(self):
		
		while True:
			receptionsocket = socket.socket()
			receptionsocket.bind(("localhost", self.port))
			receptionsocket.listen()
			client, address = receptionsocket.accept()
			#self.receptionsocket.bind(("localhost", self.port)) #on le met ici pour que l'action soit réitérée à chaque boucle  d'abor envoyer et puis écouter
			#self.receptionsocket.listen()	
			#client, address = self.receptionsocket.accept()
			reception = True
			etatserv = ""
			
			print('test')
			while reception:

				messageread = ""
				etatserv = ""
				
				etatserv = client.recv(4096).decode('utf8')
				if etatserv != "":
					messageread = json.loads(etatserv)
					print(messageread)
					
					reception = False
			reception = True
			if messageread == 	{"request": "ping"}:
				pong = {"response": "pong"}
				pongencode = json.dumps(pong)
				client.send(pongencode.encode('utf8'))
				print('ok')
		client.close()
			


			#on crée une boucle qui écoute et qui vérifie si le message reçu est vide

			
othelloIA().inscription()
