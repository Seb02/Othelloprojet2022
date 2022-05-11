import sys
import json
import socket
import random
import time

def add(p1, p2):
		l1, c1 = p1
		l2, c2 = p2
		return l1 + l2, c1 + c2 
		
def coord(index):
		return index // 8, index % 8

def Coupchoisi(casesprises, mouvementspossibles, state):
		
	liste0 = [1, 8, 6, 15, 48, 57, 62, 55]
	liste1 = [9, 14, 49, 54]
	liste2 = [ 11, 12, 25, 30, 33, 38, 51, 52]
	liste3 = [19, 20, 26, 29, 34, 37, 43, 44]
	liste4 =  [3, 4, 24, 31, 32, 39, 59, 60]
	liste5 = [2, 10, 18, 17, 16, 40, 41, 42, 50, 58, 61, 53, 45, 46, 47, 5, 13, 21, 22, 23]
	liste6 = [0, 7, 56, 63]
	listetot = liste6 + liste4
	coupspris = []
	i = 0
	print('test1')
	print(casesprises)
	for elem in casesprises:
		
		if elem in listetot:
			
			i+=1
			if i>=12 :	
				print('TestMaxCoup')	
				for elembis in mouvementspossibles:
					coupspris.append(len(WillBeTaken(state, elembis)))
					maxindex = coupspris.index(max(coupspris))
					return mouvementspossibles[maxindex]
			
	print('test3')
	listeElem6 = []
	for elem in mouvementspossibles:
		if elem in liste6:
			listeElem6.append(elem)
	
	listeElem5 = []
	for elem in mouvementspossibles:
		if elem in liste5:
			listeElem5.append(elem)
	
	listeElem4 = []
	for elem in mouvementspossibles:
		if elem in liste4:
			listeElem4.append(elem)
	
	listeElem3 = []
	for elem in mouvementspossibles: 
		if elem in liste3:
			listeElem3.append(elem)
	
	listeElem2 = []
	for elem in mouvementspossibles:
		if elem in liste2:
			listeElem2.append(elem)
	
	listeElem1 = []
	for elem in mouvementspossibles:
		if elem in liste1:
			listeElem1.append(elem)
	
	listeElem0 = []
	for elem in mouvementspossibles:
		if elem in liste0:
			listeElem0.append(elem)
	
	if len(listeElem6)>0:
		return MoinsDeMouvPoss(listeElem6, state)
	if len(listeElem5)>0:
		return MoinsDeMouvPoss(listeElem5, state)
	if len(listeElem4)>0:
		return MoinsDeMouvPoss(listeElem4, state)
	if len(listeElem3)>0:
		return MoinsDeMouvPoss(listeElem3, state)
	if len(listeElem2)>0:
		return MoinsDeMouvPoss(listeElem2, state)
	if len(listeElem1)>0:
		return MoinsDeMouvPoss(listeElem1, state)
	if len(listeElem0)>0:
		return MoinsDeMouvPoss(listeElem0, state)
	else:
		return random.choice(mouvementspossibles)


def WillBeTaken(state, move):
	playerIndex = state['current']
	otherIndex = (playerIndex+1)%2
	if not (0 <= move < 64):
		raise BadMove('Your must be between 0 inclusive and 64 exclusive')
	if move in state['board'][0] + state['board'][1]:
		raise BadMove('This case is not free')
	board = []
	for i in range(2):
		board.append(set((coord(index) for index in state['board'][i])))
	move = coord(move)
	
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
		for case in walk(move, direction):
			if case in board[otherIndex]:
				mayBe.add(case)
			elif case in board[playerIndex]:
				cases |= mayBe
				break
			else:
				break
	if len(cases) == 0:
		raise BadMove('Your move must take opponent\'s pieces')

	return [index(case) for case in cases]



def index(coord):
	l, c = coord
	return l*8+c



def isInside(coord):
	l, c = coord
	return 0 <= l < 8 and 0 <= c < 8

def walk(start, direction):
		current = start
		while isInside(current):
			current = add(current, direction)
			yield current

def MoinsDeMouvPoss(listemvts, state):

	
		coupspris = []
		for elem in listemvts:
			coupspris.append(len(WillBeTaken(state, elem)))
			minindex = coupspris.index(min(coupspris))
			print(minindex)
			print(coupspris)
			print(len(coupspris))
			print(len(listemvts))
			print(listemvts[minindex])
		return listemvts[minindex]

def PossibleMoves(state):
		res = []
		for move in range(64):
			try:
				WillBeTaken(state, move)
				res.append(move)
			except BadMove:
				pass
		return res

class BadMove(Exception): #pour définir une erreur d'un type défini
	pass
	
			


	
	
	

#test

