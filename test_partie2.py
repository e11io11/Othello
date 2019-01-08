from partie2 import *

#pion_adverse:

print("test pion_adverse:")
print(pion_adverse(1) == 2)
print(pion_adverse(2) == 1)
print("")



#prise_possible_direction:

print("test prise_possible_direction:")
p = creer_plateau(4)
print(prise_possible_direction(p,1,3,0,-1,2) == True)
print(prise_possible_direction(p,1,3,0,-1,1)  == False)
print(prise_possible_direction(p,1,3,-1,-1,2) == False)
print(prise_possible_direction(p,1,0,0,1,1)   == True)
print("")



#mouvement_valide:

print("test mouvement_valide:")
p = creer_plateau(4)
print(mouvement_valide(p,1,3,2) == True)
print(mouvement_valide(p,0,0,1) == False)
print("")



#mouvement_direction:

print("test mouvement_direction:")
p = creer_plateau(4)
mouvement_direction(p,0,3,-1,1,2) # ne modifie rien
print(p =={'n': 4, 'cases': [0, 0, 0, 0,
                             0, 2, 1, 0,
                             0, 1, 2, 0,
                             0, 0, 0, 0]})
mouvement_direction(p,1,3,0,-1,2) # met la valeur 2 dans les cases (1,2) et (1,3)
print(p =={'n': 4, 'cases': [0, 0, 0, 0,
                             0, 2, 2, 2,
                             0, 1, 2, 0,
                             0, 0, 0, 0]})
print("")



#mouvement:

print("test mouvement:")
p = creer_plateau(4)
mouvement(p,0,3,2) # ne modifie rien
print(p =={'n': 4, 'cases': [0, 0, 0, 0,
                             0, 2, 1, 0,
                             0, 1, 2, 0,
                             0, 0, 0, 0]})
mouvement(p,1,3,2) # met la valeur 2 dans les cases (1,2) et (1,3)
print(p == {'n': 4, 'cases': [0, 0, 0, 0,
                              0, 2, 1, 0,
                              0, 1, 2, 0,
                              0, 0, 0, 0]})
print("")



#joueur_peut_jouer:

print("joueur_peut_jouer:")
p = creer_plateau(4)
print(joueur_peut_jouer(p,1) == True)
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,1,1,1)
set_case(p,2,2,1)
print(joueur_peut_jouer(p,1) == False)
print("")



#fin_de_partie:

print("fin_de_partie:")
p = creer_plateau(4)
print(fin_de_partie(p) == False)
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,1,1,1)
set_case(p,2,2,1)
print(fin_de_partie(p) == True)
print("")



#gagnant:

print("gagnant:")
p = creer_plateau(4)
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,1,1,1)
set_case(p,2,2,1)
print(gagnant(p) == 1)
