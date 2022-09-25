def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")
        print(f'Seu saldo atual e: {saldo}.')
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f'Seu saldo atual e: {saldo}.')

depositar(600)
sacar(200)

