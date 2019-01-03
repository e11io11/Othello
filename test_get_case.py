from partie1 import *
plateau={}

plateau["n"]=4
plateau["cases"]=[0, 0, 1, 0,
                  2, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 3, 0]

print(get_case(plateau,0,2)==1)
print(get_case(plateau,1,0)==2)
print(get_case(plateau,3,2)==3)


plateau["n"]=6
plateau["cases"]=[0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 2, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  3, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 1, 0]

print(get_case(plateau,5,4)==1)
print(get_case(plateau,2,2)==2)
print(get_case(plateau,4,0)==3)


plateau["n"]=8
plateau["cases"]=[2, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 3, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 1]

print(get_case(plateau,7,7)==1)
print(get_case(plateau,0,0)==2)
print(get_case(plateau,5,6)==3)

get_case(plateau,-1,0) #renvoie une erreur
