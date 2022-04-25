import socket
import sys
import json
import socket

class othelloIA: #initialsation du socket 
	def __init__(self, ipbut = "localhost", port = 2048 ): #port 2048 : utilisé en local quand l'ordi se comporte comme serveur
		self.port = port
		self.ipbut = ipbut
		self.name = "IA2003420342"
		self.matricule1 = "20034"
		self.matricule2 = "20342"
		self.s = socket.socket()  
		serverAddress = (self.ipbut, 3000) #port 3000 : utilisé pour atteindre le serveur de gestion des jeux
		self.s.connect(serverAddress)
		self.color = ""
		#self.receptionsocket = socket.socket()
		
		
		
		
		
	
	def inscription(self):

		renseignements = json.dumps({
   		"request": "subscribe",
   		"port": self.port,
   		"name": self.name,
   		"matricules": [self.matricule1, self.matricule2]
		}) #json.dumps() function converts a Python object into a json string.
		self.s.send(renseignements.encode('utf8'))
		self.PingPong()
		self.couleurjoueur = ""
	def PingPong(self):
		
		while True:
			receptionsocket = socket.socket()
			receptionsocket.bind(("localhost", self.port))
			receptionsocket.listen()
			client, address = receptionsocket.accept()
			
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
			if messageread["request"] == "play":
				if messageread["players"][0] == self.name:
					self.color = black
				else:
					self.color = white
				self.etatjeu(self.color)
		client.close()

	def etatjeu(self, color ):
		for i in range (64):
			pass

	def mouvementspossibles(self, board):
		pass




			#on crée une boucle qui écoute et qui vérifie si le message reçu est vide

			
othelloIA().inscription()
