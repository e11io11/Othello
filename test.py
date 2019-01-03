from partie2 import *

p = creer_plateau(8)
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,3,5,1)
set_case(p,3,6,1)
mouvement(p,3,7,2)
afficher_plateau(p) # retourne 1
