from partie1 import *

plateau={}



plateau["n"]=4
plateau["cases"]=[0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0]

set_case(plateau, 0, 0, 2)
set_case(plateau, 2, 3, 0)
set_case(plateau, 0, 1, 1)

print(get_case(plateau, 0, 0)==2)
print(get_case(plateau, 2, 3)==0)
print(get_case(plateau, 0, 1)==1)



plateau["n"]=6
plateau["cases"]=[0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0]

set_case(plateau, 5, 3, 1)
set_case(plateau, 2, 1, 2)
set_case(plateau, 0, 4, 0)

print(get_case(plateau, 5, 3)==1)
print(get_case(plateau, 2, 1)==2)
print(get_case(plateau, 0, 4)==0)



plateau["n"]=8
plateau["cases"]=[0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0]

set_case(plateau, 7, 7, 1)
set_case(plateau, 2, 4, 0)
set_case(plateau, 1, 7, 2)

print(get_case(plateau, 7, 7)==1)
print(get_case(plateau, 2, 4)==0)
print(get_case(plateau, 1, 7)==2)


set_case(plateau, 9, 2, 1) #renvoie une erreur
set_case(plateau, 0, 0, 3) #renvoie une erreur
