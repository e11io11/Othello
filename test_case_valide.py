from partie1 import *

plateau={"n":4}

print(case_valide(plateau, 0,3)==True)
print(case_valide(plateau, 3,4)==False)
print(case_valide(plateau, 5,2)==False)


plateau={"n":6}

print(case_valide(plateau, 2,1)==True)
print(case_valide(plateau, 3,5)==True)
print(case_valide(plateau, 8,6)==False)


plateau={"n":8}

print(case_valide(plateau, 1,7)==True)
print(case_valide(plateau, 8,8)==False)
print(case_valide(plateau, -2,0)==False)
