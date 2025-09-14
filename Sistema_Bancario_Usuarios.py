#Sistema Bancário com uso de datas (v2)

from datetime import datetime

#====================#

def verificacao_cpf(Usuarios, cpf):
    for user in Usuarios:
        if user["cpf"] == cpf:
            return user
    return None

def Criar_Usuario(Usuarios):
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")

    cpf = input("Digite seu CPF (somente numeros): ")
    if verificacao_cpf(Usuarios, cpf) is not None:
        print("cpf já existente")
        return

    endereco = input("Digite seu Endereço: ")

    Usuarios.append({
        "Nome": nome,
        "Data de nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    })
    print(f"Usuário Cadastrado\n{Usuarios}")

def Criar_conta(Usuarios, Conta,numero_conta ):
    cpf = input("Digite seu cpf: ")
    usuario = verificacao_cpf(Usuarios, cpf)

    if usuario is None:
        print("Não foi achado seu usuário\nTente criar um usuário antes!")
    else:
        numero_conta += 1
        Conta.append({
        "Agência": "0001",
        "Número da Conta": numero_conta,
        "CPF": cpf,
        })
        print(Conta)
        return numero_conta

def Listar_contas(Conta):
    if not Conta:
        print("Nenhuma conta criada ainda!")
        return
    
    for user in Conta:
            print(user)

def Deposito(Extrato, Saldo, limite_transacoes):
    valor_depositar = float(input("Depósito\nDigite um valor a ser depositado: "))

    if valor_depositar <= 0:
        print("Valor Inválido.")
        return Saldo, limite_transacoes
    
    elif valor_depositar > 0:
        Saldo += valor_depositar
        limite_transacoes += 1

        Extrato.append({
            "Tipo": "Depósito",
            "Valor": f"{valor_depositar:.2f}",
            "Horário": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        })

        print("Depósito Concluído.")
        return Saldo, limite_transacoes

def Saque(Extrato, Saldo, saque_atual, limite_transacoes): 
    while True:
        if saque_atual >= 3:
            print("Você já sacou a quantia máxima permitida em um dia, volte amanhã!")
            return Saldo, saque_atual, limite_transacoes
       

        valor_saque = float(input(f"Saque({saque_atual + 1})\nDigite o valor a ser sacado: "))
        
        if valor_saque > 500 or valor_saque <= 0 or valor_saque > Saldo:
            print("Valor Inválido.")
        
        elif valor_saque <= Saldo:
            Saldo -= valor_saque
            saque_atual += 1
            limite_transacoes += 1

            Extrato.append({
                "Tipo": "Saque",
                "Valor": f"{valor_saque:.2f}",
                "Horário": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            })

            print("Saque Concluído.")
            return Saldo, saque_atual, limite_transacoes

def Mostrar_extrato(Extrato, Saldo):
    print("Extrato\n==========")
    if len(Extrato) == 0:
        print("Nenhuma transação foi realizada.")
    else:
        for transacao in Extrato:
            print(f"{transacao["Tipo"]} -> \tR$:{transacao["Valor"]} \t{transacao["Horário"]}")
            
        print(f"----------\nSaldo Atual:\t R$ {Saldo:.2f}\n========== ")

def main():
    #========== VARIAVEIS ==========#
    Usuarios = []
    Conta = []
    Saldo = 0
    Extrato = []
    saque_atual = 0
    limite_transacoes = 0
    numero_conta = 0
    #========== MENU ===========#
    menu = """
    [c] Cadastro de Usuário
    [r] Criar Conta
    [l] Listar contas
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu).lower()

        if opcao == "c":
            Criar_Usuario(Usuarios)

        elif opcao == "r":
            numero_conta = Criar_conta(Usuarios, Conta, numero_conta)

        elif opcao == "l":
            Listar_contas(Conta)

        elif opcao == "d":
            if limite_transacoes < 10:
                Saldo, limite_transacoes = Deposito(Extrato, Saldo, limite_transacoes)
            else:
                print("Você excedeu o número de transações permitidas no dia.\n Tente novamente amanhã.")
            
        elif opcao == "s":
            if limite_transacoes < 10:
                Saldo, saque_atual, limite_transacoes = Saque(Extrato, Saldo, saque_atual, limite_transacoes)
            else:
                print("Você excedeu o número de transações permitidas no dia.\n Tente novamente amanhã.")

        elif opcao == "e":
            Mostrar_extrato(Extrato, Saldo)
            
        elif opcao == "q":
            break

        else:
            print("Operação Inválida, tente novamente.")

if __name__ == "__main__":
    main()