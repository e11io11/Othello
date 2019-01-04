from partie2 import *

p = creer_plateau(6)
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,2,4,1)
mouvement(p,2,5,2)
afficher_plateau(p) # retourne 1
