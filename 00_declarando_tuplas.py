frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",) #virgula no final para evitar confusão na precedencia de operadores.
print(pais)

carros = ("gol")
print(isinstance(carros, tuple))
