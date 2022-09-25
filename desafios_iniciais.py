#entrada = input().split()

'''
distancia = int(input("informe a distancia: "))
diametro1 = int(input("informe o diametro1: "))
diametro2 = int(input("informe o diametro2: "))

print(f"O ICM e: {distancia / (diametro1 + diametro2):.2f}")
'''

#entrada = [100, 2, 2]

#distancia = int(entrada[0])
#diametro1 = int(entrada[1])
#diametro2 = int(entrada[2])

from audioop import avg
from statistics import mean


'''
lista = [100, 2]
print((lista[0]) / (lista[1]))
print(f"{(lista[0]) / (lista[1]):.2f}")

var1 = int(input())
var2 = int(input())
total = var1 / var2

print(f"{total:.2f}")
'''

valores = input().split()
valores = list(map(int, valores))



#print(list(map(int, valores)))
print(valores)
print(f"{((valores[0]) * (valores[1])/12):.3f}")