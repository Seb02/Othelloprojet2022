import socket
import sys
import json
import socket
import random

class othelloIA: #initialsation du socket 
	def __init__(self, ipbut = "localhost" ): #localhost pour jouer en local, sinon, ip du serveur 
		self.port = int(input("Port, 2048 si vide ") or 2048)
		self.ipbut = ipbut
		self.name = input("Nom IA, IA2003420342 si vide ") or "IA2003420342" #permet de donner une valeur par défaut aux input
		self.matricule1 =  input("matricule 1, 20034 si vide ") or "20034"
		self.matricule2 = input("matricule 2, 20342 si vide ") or "20342"
		self.s = socket.socket()  
		serverAddress = (self.ipbut, 3000) #port 3000 : utilisé pour atteindre le serveur de gestion des jeux
		print(serverAddress)
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
			receptionsocket.bind(("0.0.0.0", self.port)) #pour écouter sur toutes nos interfaces réseau
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
			print("test2")
			if messageread == 	{"request": "ping"}:
				pong = {"response": "pong"}
				pongencode = json.dumps(pong)
				client.send(pongencode.encode('utf8'))
				print('ok')
			if messageread["request"] == "play":
				
				self.Couleurjoueur(messageread)

				jeunoir = messageread['state']["board"][0]
				jeublanc = messageread['state']["board"][1]
				
				
				self.PossibleMoves(messageread['state'])

				if len(self.mouvementspossibles) > 0:
					mouvement = self.Coupchoisi()
					reponse = {"response": "move", "move": mouvement, "message": "Fun message"}
					mouvementaenvoyer = json.dumps(reponse)
					client.send(mouvementaenvoyer.encode('utf8'))
				else :
					reponse = {"response": "giveup",}
					mouvementaenvoyer = json.dumps(reponse)
					client.send(mouvementaenvoyer.encode('utf8')) 

		client.close()

	
			
	def Couleurjoueur (self, message):
		
		listejoueurs = message['state']['players']
		if listejoueurs[0] == self.name:
			self.color = "black"
					
		else:
			self.color = "white"

	
	
	def Coupchoisi(self):

		return random.choice(self.mouvementspossibles)

	def WillBeTaken(self, state, move):
		playerIndex = state['current']
		otherIndex = (playerIndex+1)%2

		if not (0 <= move < 64):
			raise BadMove('Your must be between 0 inclusive and 64 exclusive')

		if move in state['board'][0] + state['board'][1]:
			raise BadMove('This case is not free')

		board = []
		for i in range(2):
			board.append(set((self.coord(index) for index in state['board'][i])))

		move = self.coord(move)
		

		cases = set()

		directions = [
		( 0,  1),
		( 0, -1),
		( 1,  0),
		(-1,  0),
		( 1,  1),
		(-1,  1),
		( 1, -1),
		(-1, -1)
		]
		for direction in directions:
			mayBe = set()
			for case in self.walk(move, direction):
				if case in board[otherIndex]:
					mayBe.add(case)
				elif case in board[playerIndex]:
					cases |= mayBe
					break
				else:
					break

		if len(cases) == 0:
			raise BadMove('Your move must take opponent\'s pieces')
	
		return [self.index(case) for case in cases]

	def index(self, coord):
		l, c = coord
		return l*8+c

	def isInside(self, coord):
		l, c = coord
		return 0 <= l < 8 and 0 <= c < 8	

	def walk(self, start, direction):
		current = start
		while self.isInside(current):
			current = self.add(current, direction)
			yield current


	def PossibleMoves(self, state):
		res = []
		for move in range(64):
			try:
				self.WillBeTaken(state, move)
				res.append(move)
			except BadMove:
				pass
		self.mouvementspossibles = res



	def coord(self, index):
		return index // 8, index % 8


	def add(self, p1, p2):
		l1, c1 = p1
		l2, c2 = p2
		return l1 + l2, c1 + c2 
		
		

	
class BadMove(Exception): #pour définir une erreur d'un type défini
	pass




			#on crée une boucle qui écoute et qui vérifie si le message reçu est vide

#test
othelloIA().inscription()
