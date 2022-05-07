import socket
import sys
import json
import socket
import random
import time

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
		
		self.etatcoups = ""
		self.state = ""
		self.casesprises = ""


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
			
			
			while reception:

				messageread = ""
				etatserv = ""
				
				etatserv = client.recv(4096).decode('utf8')
				if etatserv != "":
					messageread = json.loads(etatserv)
					print(messageread)
					
					reception = False
			
			if messageread == 	{"request": "ping"}:
				pong = {"response": "pong"}
				pongencode = json.dumps(pong)
				client.send(pongencode.encode('utf8'))
				print('ok')
			if messageread["request"] == "play":
				
				

				self.state = messageread['state']
				self.casesprises = messageread['state']['board'][0]+messageread['state']['board'][1]
				
				
				self.PossibleMoves(self.state)
				self.etatcoups = messageread['state']

				if len(self.mouvementspossibles) > 0:
					
					mouvement = self.Coupchoisi()
					reponse = {"response": "move", "move": mouvement, "message": "Fun message"}
					mouvementaenvoyer = json.dumps(reponse)
					client.send(mouvementaenvoyer.encode('utf8'))
				else :
					reponse = {"response": "move", "move": None, "message": "Fun message"}
					mouvementaenvoyer = json.dumps(reponse)
					client.send(mouvementaenvoyer.encode('utf8')) 

		client.close()

	
			


	
	
	def Coupchoisi(self):
		
		liste0 = [1, 8, 6, 15, 48, 57, 62, 55]
		liste1 = [9, 14, 49, 54]
		liste2 = [ 11, 12, 25, 30, 33, 38, 51, 52]
		liste3 = [19, 20, 26, 29, 34, 37, 43, 44]
		liste4 =  [3, 4, 24, 31, 32, 39, 59, 60]
		liste5 = [2, 10, 18, 17, 16, 40, 41, 42, 50, 58, 61, 53, 45, 46, 47, 5, 13, 21, 22, 23]
		liste6 = [0, 7, 56, 63]
		coupspris = []
		i = 0
		print('test1')
		print(self.casesprises)
		for elem in self.casesprises:
			
			if elem in liste6 or elem in liste4:
				
				i+=1
				if i>=12  and len(self.casesprises)>=58:	
					print('Test2')	
					for elembis in self.mouvementspossibles:
						coupspris.append(len(self.WillBeTaken(self.state, elembis)))
						maxindex = coupspris.index(max(coupspris))
						return self.mouvementspossibles[maxindex]

		print('test3')
		listeElem6 = []

		for elem in self.mouvementspossibles:
			if elem in liste6:
				listeElem6.append(elem)
		
		listeElem5 = []
		for elem in self.mouvementspossibles:
			if elem in liste5:
				listeElem5.append(elem)
		
		listeElem4 = []
		for elem in self.mouvementspossibles:
			if elem in liste4:
				listeElem4.append(elem)
		
		listeElem3 = []
		for elem in self.mouvementspossibles: 
			if elem in liste3:
				listeElem3.append(elem)
		
		listeElem2 = []
		for elem in self.mouvementspossibles:
			if elem in liste2:
				listeElem2.append(elem)
		
		listeElem1 = []
		for elem in self.mouvementspossibles:
			if elem in liste1:
				listeElem1.append(elem)
		
		listeElem0 = []
		for elem in self.mouvementspossibles:
			if elem in liste0:
				listeElem0.append(elem)
		
		if len(listeElem6)>0:
			return self.MoinsDeMouvPoss(listeElem6)
		if len(listeElem5)>0:
			return self.MoinsDeMouvPoss(listeElem5)
		if len(listeElem4)>0:
			return self.MoinsDeMouvPoss(listeElem4)
		if len(listeElem3)>0:
			return self.MoinsDeMouvPoss(listeElem3)
		if len(listeElem2)>0:
			return self.MoinsDeMouvPoss(listeElem2)
		if len(listeElem1)>0:
			return self.MoinsDeMouvPoss(listeElem1)
		if len(listeElem0)>0:
			return self.MoinsDeMouvPoss(listeElem0)
		else:
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

	def MoinsDeMouvPoss(self, listemvts):

	
		coupspris = []
		for elem in listemvts:
			coupspris.append(len(self.WillBeTaken(self.state, elem)))
			minindex = coupspris.index(min(coupspris))
			print(minindex)
			print(coupspris)
			print(len(coupspris))
			print(len(listemvts))
			print(listemvts[minindex])
		return listemvts[minindex]
		
			


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
