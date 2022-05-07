# IA Othello (IA_20034_20342)

## Contenu du répositoire 
* Un fichier ... contenant...
* Un fichier ... contenant...
* Un fichier ... contenant...

## Description de l'IA

l'objectif de ce travail est la réalisation d'une IA capable de jouer des parties de Othello, un jeu de plateau à deux joueurs, voir [Règles du jeu](https://www.ffothello.org/othello/regles-du-jeu/).
Les capacités de l'IA ont été priorisées comme suit : 
1. Respecter en tout temps les règles du jeu
2. Battre un joueur plaçant ses coups de manière aléatoire 
3. Jouer ses propres coups dans un minimum de temps (<10s)

La stratégie établie est la suivante 
- Dans un premier temps l'objectif est de controler des cases statégiquements importantes du jeu à savoir les quatres coins ainsi que certaines cases sur les bords. la priorité des coups est définie par des listes d'importances, représentées sur la figure 1. Lorsque plusieurs choix sont équivalent celui qui retourne le moins de pions est choisi en priorité afin de laisser le moins de possibilités de coups à l'adversaire. Cette strégie est adoptée tant que les cases des listes 5 et 6 ne sont pas intégralement controlées 
- Une fois les cases des listes 5 et 6 contrôlés la méthode de jeu change, l'objectif est maintenant de retourner le plus de pions possibles et l'IA sélectionne donc uniquement le choix qui rapporte le plus de points.
 

![Othello](https://user-images.githubusercontent.com/99732004/167264240-cfc4e1be-51b6-4b25-9800-9d3ae33bb71e.png)

## Lancement du programme

En lancant le programme, 4 inputs sont envoyés à l'utilisateur, ils contiennent par défaut les éléments nécessaires au lancement du programme.
Le premier input contient le port sur lequel le client écoute le serveur (2048), le second contient le nom sous lequel s'inscrit le client (IA_20034_20342). Les deux derniers contiennent les matricules des deux auteurs de l'IA. 

