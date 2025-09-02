#Sistema Bancário simples de Deposito, Saque e Extrato (v1)

Conta = 0
Extrato = ""
saque_atual = 0

def Deposito():
    global Conta, Extrato
    valor_depositar = float(input("Depósito\nDigite um valor a ser depositado: "))

    if valor_depositar <= 0:
        print("Valor Inválido.")
    
    elif valor_depositar > 0:
        Conta += valor_depositar
        Extrato += f"Depósito: R$ {valor_depositar:.2f}\n"
        print("Depósito Concluído.")

def Saque():
    global Conta, Extrato, saque_atual
    
    while True:
        if saque_atual == 3:
            print("Você já sacou a quantia máxima permitida em um dia, volte amanhã!")
            break

        valor_saque = float(input(f"Saque({saque_atual + 1})\nDigite o valor a ser sacado: "))
        
        if valor_saque > 500 or valor_saque < 0 or valor_saque > Conta:
            print("Valor Inválido.")
        
        elif valor_saque <= Conta:
            Conta -= valor_saque
            Extrato += f"Saque: R$ {valor_saque:.2f}\n"
            saque_atual += 1
            print("Saque Concluído.")
            break

menu = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> """

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        Deposito()
        
    elif opcao == "s":
        Saque()

    elif opcao == "e":
        print(f"Extrato:\n{Extrato}")
        print(f"Saldo Atual:\n{Conta} ")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, tente novamente.")     