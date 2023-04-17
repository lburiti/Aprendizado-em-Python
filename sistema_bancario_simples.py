
from time import sleep


conta_normal = ()
conta_universitaria = ()
saldo = 2000
cheque_especial = 450
print("#" * 35)
print()
print(" " * 1, "Bem vindo ao sistema bancário!!")
print()
print("#" * 35)
print()
sleep(1);

tipo_conta = input("Selecione o tipo de conta: (n) conta normal / (u) conta universitaria: ")
sleep(1);

if tipo_conta == "n":
    conta_normal = True
    print("\nConta Normal Selecionada!\n")
    print(f'Seu saldo atual e: {saldo}\n')
    print(f'Seu limite de cheque especial e: {cheque_especial}\n')
    saque = int(input("Informe o valor a retirar: "))
elif tipo_conta == "u":
    conta_universitaria = True
    print("\nConta Universitaria Selecionada!\n")
    print(f'Seu saldo atual e: {saldo}\n')
    print(f'Seu limite de cheque especial e: {cheque_especial}\n')
    saque = int(input("Informe o valor a retirar: "))

if conta_normal:
    if saldo >= saque:
        saldo = saldo - saque
        print("Saque realizado com sucesso!")
        print(f'Seu saldo atual e: {saldo}')
    elif saque <= (saldo + cheque_especial):
        #saldo = saldo - saque
        print("Saque realizado com uso do cheque especial!")
        print(f'Seu saldo atual e: {(saldo + cheque_especial) - saque}')
    else:
        #saldo = saldo - saque
        print("Não for possivel realizar o saque!")
        print(f'Para sua solicitacao de retirada de {saque} seu saldo + cheque especial e: {saldo + cheque_especial}')
        print(f'Seu saldo ficaria negativo em: {(saldo + cheque_especial) - saque}')
elif conta_universitaria:
    if saldo >= saque:
        saldo = saldo - saque
        print("Saque realizado com sucesso!")
        print(f'Seu saldo atual e: {saldo}')
    elif saque <= (saldo + cheque_especial):
        #saldo = saldo - saque
        print("Saque realizado com uso do cheque especial!")
        print(f'Seu saldo atual e: {(saldo + cheque_especial) - saque}')
    else:
        print("Saldo insuficiente!")
        print(f'Para sua solicitacao de retirada de {saque} seu saldo + cheque especial e: {saldo + cheque_especial}')
        print(f'Seu saldo ficaria negativo em: {(saldo + cheque_especial) - saque}')
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente!")
