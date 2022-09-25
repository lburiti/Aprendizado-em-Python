lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]

numeros = []
quadrado = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(quadrado)