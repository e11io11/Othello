from partie1 import *

plateau=creer_plateau(4)
print(plateau=={"n":4,
                "cases":[0, 0, 0, 0,
                         0, 2, 1, 0,
                         0, 1, 2, 0,
                         0, 0, 0, 0]})

plateau=creer_plateau(6)
print(plateau=={"n":6,
                "cases":[0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0,
                         0, 0, 2, 1, 0, 0,
                         0, 0, 1, 2, 0, 0,
                         0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0]})

plateau=creer_plateau(8)
print(plateau=={"n":8,
                "cases":[0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 2, 1, 0, 0, 0,
                         0, 0, 0, 1, 2, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0]})



plateau=creer_plateau(9) #renvoie une erreur
