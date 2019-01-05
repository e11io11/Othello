from partie3 import *


#Test creer_partie:

print("creer_partie:")
print(creer_partie(4) == {
                          'plateau': {
                                      'n': 4,
                                      'cases': [0, 0, 0, 0,
                                                0, 2, 1, 0,
                                                0, 1, 2, 0,
                                                0, 0, 0, 0]
                                     },
                          'joueur': 1
                          })


print(creer_partie(8) == {
                          'plateau': {
                                      'n': 8,
                                      'cases': [0, 0, 0, 0, 0, 0, 0, 0,
                                                0, 0, 0, 0, 0, 0, 0, 0,
                                                0, 0, 0, 0, 0, 0, 0, 0,
                                                0, 0, 0, 2, 1, 0, 0, 0,
                                                0, 0, 0, 1, 2, 0, 0, 0,
                                                0, 0, 0, 0, 0, 0, 0, 0,
                                                0, 0, 0, 0, 0, 0, 0, 0,
                                                0, 0, 0, 0, 0, 0, 0, 0]
                                      },
                          'joueur': 1
                         })
print("")



#Test saisie_valide:

print("saisie_valide:")
p = creer_partie(4)
print(saisie_valide(p, "M") == True)
print(saisie_valide(p, "b1") == True)
print(saisie_valide(p, "b4") == False)
print("")
