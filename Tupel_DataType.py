# We cant change the the in Tuple after it crated.... it's like constant 

from typing import Tuple


# Tuple
Tupl=(1,8,5,"hey","world",2,3,6)
print(len(Tupl))            #This prints the length of an array ["len" =  length]
print(Tupl)
print(Tupl[2])
listt=list(Tupl)
listt[1]="Rushikesh"
Tupl=tuple(listt)
print(Tupl)

# del Tupl       #It will delete tuple