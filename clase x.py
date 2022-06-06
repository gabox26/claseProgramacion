import numpy as np
import random


arreglo = np.diag([1,1,1])

print(arreglo)

for i in range(3):
    for j in range(3):
        print(arreglo[i][j])
        
        
for i in range(3):
    for j in range(3):
        arreglo[i][j] = random.randint(0,100)
        

print(arreglo)
    
        

