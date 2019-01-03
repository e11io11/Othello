from partie1 import *

plateau={"n":4}

print(indice_valide(plateau, 0)==True)
print(indice_valide(plateau, 3)==True)
print(indice_valide(plateau, 4)==False)


plateau={"n":6}

print(indice_valide(plateau, 0)==True)
print(indice_valide(plateau, 5)==True)
print(indice_valide(plateau, 8)==False)


plateau={"n":8}

print(indice_valide(plateau, 6)==True)
print(indice_valide(plateau, -1)==False)
print(indice_valide(plateau, 9)==False)
