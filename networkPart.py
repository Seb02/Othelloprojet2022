import socket
import sys
import json
import socket
import random
import time
import ia

class othelloIA: #initialsation du socket 
	def __init__(self, ipbut = "localhost" ): #localhost pour jouer en local, sinon, ip du serveur 

		####Manière de lancer modifiée suite au changement de programme (pas de partie en ligne mais en local)####


		# = int(input("Port, 2048 si vide ") or 2048) 
		self.port = int(sys.argv[1]) #permet de choisir le port 
		self.ipbut = ipbut
		#self.name = input("Nom IA, IA_20034_20342 si vide ") or "IA_20034_20342" #permet de donner une valeur par défaut aux input
		#self.matricule1 =  input("matricule 1, 20034 si vide ") or "20034"
		#self.matricule2 = input("matricule 2, 20342 si vide ") or "20342"
		self.name = "IA_20034_20342"
		self.matricule1 = "20034"
		self.matricule2 = "20342"

		self.s = socket.socket()  
		serverAddress = (self.ipbut, 3000) #port 3000 : utilisé pour atteindre le serveur de gestion des jeux
		print(serverAddress)
		self.s.connect(serverAddress)
		
		self.etatcoups = ""
		self.state = ""
		self.casesprises = ""
		

		
		
		
		
		
		
	
	def inscription(self): #gère la partie réseau et appelle les fonctions de calcul de coups

		renseignements = json.dumps({
		   "request": "subscribe",
		   "port": self.port,
		   "name": self.name,
		   "matricules": [self.matricule1, self.matricule2]
		}) #json.dumps() function converts a Python object into a json string., requête d'insciption + infos sur le client
		self.s.send(renseignements.encode('utf8'))
		self.PingPong()
		self.couleurjoueur = ""
	def PingPong(self):  #fonction qui gère les réceptions et les envois pendant la partie; que ce soit pour les ping ou les coups
		
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
				
				etatserv = client.recv(4096).decode('utf8') #réception du message envoyé par le serveur
				if etatserv != "":
					messageread = json.loads(etatserv)
					print(messageread)
					
					reception = False
			
			if messageread == 	{"request": "ping"}: #réponse à la requête ping
				pong = {"response": "pong"}
				pongencode = json.dumps(pong)
				client.send(pongencode.encode('utf8'))
				print('ok')
			if messageread["request"] == "play": #réponse à la requête de coups
				
				

				
				self.casesprises = messageread['state']['board'][0]+messageread['state']['board'][1]  #défini la liste des cases prises, ce qui permet à l'ia de calculer le coup choisi
				
				
				mouvementsPossibles =ia.PossibleMoves(messageread['state'])  #appelle à la fonction possible moves, contenue à l'origine dans le fichier game.py du getionnaire de partie
				self.etatcoups = messageread['state']

				if len(mouvementsPossibles) > 0:  #joue un coup seuelemnt si c'est possible 
					
					mouvement = ia.Coupchoisi(self.casesprises, mouvementsPossibles, self.etatcoups)
					reponse = {"response": "move", "move": mouvement, "message": "Fun message"}
					mouvementaenvoyer = json.dumps(reponse)
					client.send(mouvementaenvoyer.encode('utf8'))
				else :
					reponse = {"response": "move", "move": None, "message": "Fun message"}
					mouvementaenvoyer = json.dumps(reponse)
					client.send(mouvementaenvoyer.encode('utf8')) 

		client.close()

	
	
#on crée une boucle qui écoute et qui vérifie si le message reçu est vide

#test
othelloIA().inscription()












































