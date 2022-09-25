
'''
letra = input()

lst = ['.','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'K', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(lst.index(letra.upper()))
'''

'''
perna = input("Informe a perna: ")

while True:
    try:
        if perna == "esquerda":
            print("ingles")
        elif perna == "direita":
            print("frances")
        elif perna == "nenhuma":
            print("portugues")
        else:
            print("caiu")
        break
    except EOFError:
        break
'''
'''
pernas = {
    "esquerda": "ingles",
    "direita": "frances",
    "nenhuma": "portugues",
    "ambas": "caiu"
}

while True:
    try:
        perna = input()
        print(pernas[perna])
    except EOFError:
        break
'''
salario = int(input())

if salario > 2000:
    percentual = 5
    reajuste = (salario * percentual / 100)
    salario = salario + (salario * percentual / 100)
elif salario >= 1500.01 <= 2000:
    percentual = 10
    reajuste = (salario * percentual / 100)
    salario = salario + (salario * percentual / 100)
elif salario >= 900.01 <= 1500:
    percentual = 12
    reajuste = (salario * percentual / 100)
    salario = salario + (salario * percentual / 100)
elif salario >= 600.01 <= 900:
    percentual = 5
    reajuste = (salario * percentual / 100)
    salario = salario + (salario * percentual / 100)
else:
    percentual = 17
    reajuste = (salario * percentual / 100)
    salario = salario + (salario * percentual / 100)

print(f"Novo salario: {salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")

