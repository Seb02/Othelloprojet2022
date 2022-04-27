import socket
import sys
import json
import socket
import game
import random

class othelloIA: #initialsation du socket 
	def __init__(self, ipbut = "localhost" ): 
		self.port = int(input("Port, 2048 si vide ") or 2048)
		self.ipbut = ipbut
		self.name = input("Nom IA, IA2003420342 si vide ") or "IA2003420342"
		self.matricule1 =  input("matricule 1, 20034 si vide ") or "20034"
		self.matricule2 = input("matricule 2, 20342 si vide ") or "20342"
		self.s = socket.socket()  
		serverAddress = (self.ipbut, 3000) #port 3000 : utilisé pour atteindre le serveur de gestion des jeux
		self.s.connect(serverAddress)
		self.color = ""
		self.etatjeu = []
		for i in range(64):
			self.etatjeu.append(0)
		self.mouvementspossibles = []


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
				
				self.Couleurjoueur(messageread)

				jeunoir = messageread['state']["board"][0]
				jeublanc = messageread['state']["board"][1]
				self.Etatjeu(self.color, jeunoir, jeublanc)
				
				self.mouvementspossibles = self.Mouvementspossibles(messageread['state']["board"])

				if len(self.mouvementspossibles) > 0:
					mouvement = self.Coupchoisi()
					reponse = {"response": "move", "move": mouvement, "message": "Fun message"}
					mouvementaenvoyer = json.dumps(pong)
					client.send(mouvementaenvoyer.encode('utf8'))
				else :
					response = {"response": "giveup",}
					mouvementaenvoyer = json.dumps(pong)
					client.send(mouvementaenvoyer.encode('utf8')) 

		client.close()

	def Etatjeu(self, color, jeunoir, jeublanc):
		#jeu noir représenté par un 1, jeu blanc représenté par un 2
		for i in self.etatjeu:
			for j in jeunoir:
				if self.etatjeu[j] !=1:
					self.etatjeu[i] = 1
			for k in jeublanc:
				if self.etatjeu[k] !=2:
					self.etatjeu[i] = 2
		return self.etatjeu
			
	def Couleurjoueur (self, message):
		
		listejoueurs = message['state']['players']
		if listejoueurs[0] == self.name:
			self.color = "black"
					
		else:
			self.color = "white"

	def Mouvementspossibles(self, board):
		
		game.possibleMoves()
	
	def Coupchoisi(self):

		return random.choice(self.mouvementspossibles)
		

	
	




			#on crée une boucle qui écoute et qui vérifie si le message reçu est vide

			
othelloIA().inscription()
