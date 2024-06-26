######{ - PROVA GRAU B - Lorenzzo Willian - }######
#1)

import random

def embaralhar_array(array):
    n = len(array)
    for _ in range(n):
        #Vai sortear dois índices aleatórios (i e j) !
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        #Troca os elem. nas posições > i e j
        array[i], array[j] = array[j], array[i]
    return array

#Ex. de uso:
array = ["a", "b", "c", "d", "e"]
print("Array inicial:", array)
array_embaralhado = embaralhar_array(array)
print("Array embaralhado:", array_embaralhado)

##################################################

# ( ◑‿◑)ɔ┏🍟--🍔┑٩(^◡^ )

