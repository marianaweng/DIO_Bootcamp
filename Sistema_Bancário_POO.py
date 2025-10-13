from datetime import datetime

class Cliente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
 
    def __str__(self): #retornar ele msm
        return f"\nCliente:\t{self.nome}\nCPF:\t{self.cpf}"  

class Conta():
    #== variaveis auxiliares==#
    contas = []
    numero_conta_total = 0

    def __init__(self, cliente):
        Conta.numero_conta_total +=1
        self.cliente = cliente
        self.numero_conta = Conta.numero_conta_total
        self.saldo = 0.0
        self.extrato = []

    @classmethod #instância de classe!
    def criar_conta(cls, cliente):
        nova_conta = Conta(cliente)
        cls.contas.append(nova_conta)
        return nova_conta

    def depositar(self, valor_depositar):
        if valor_depositar <= 0:
            print("Valor Inválido.")
    
        elif valor_depositar > 0:
            self.saldo += valor_depositar
            self.extrato.append(f"Depósito:\nR$ {valor_depositar:.2f}\t{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

            print("Depósito Concluído.")

    def sacar(self, valor_saque):      
        if valor_saque > 500 or valor_saque <= 0 or valor_saque > self.saldo:
            print("Valor Inválido.")
        
        elif valor_saque <= self.saldo:
            self.saldo -= valor_saque
            self.extrato.append(f"Saque:\nR$ {valor_saque:.2f}\t{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

            print("Saque Concluído.")
    
    def exibir_extrato(self):
        print("=== Extrato ===")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
        
    def __str__(self):
        return f"""
        === Conta (#{self.numero_conta}) ===
        Nome:\t{self.cliente.nome}
        CPF:\t{self.cliente.cpf}"""
    
#==========    MAIN    ==========#    

def main():
    #   VARIÁVEIS
    clientes = []

    #   FUNCOES AUXILIARES
    def verificar_cpf(cpf):
        for cliente in clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def verificar_conta(cpf):
        for conta in Conta.contas:
            if conta.cliente.cpf == cpf:
                return conta
        return None

    #   MENU
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
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu cpf: ")

            cliente = Cliente(nome, cpf)
            clientes.append(cliente)
            print(cliente)
            print("Cadastro concluido")

        elif opcao == "r":
            cpf = input("Digite seu cpf: ")
            cpf_cliente = verificar_cpf(cpf)
            cliente = cpf_cliente

            if cpf_cliente is None:
                print("CPF do cliente nao encontrado, tente Cadastrar o usuario")

            else:
                nova_conta = Conta.criar_conta(cliente)
                print(f"\nConta({nova_conta.numero_conta}) criada!")

        elif opcao == "l":
            if not Conta.contas:
                print("Não há contas ainda")
            else:
                for conta in Conta.contas:
                    print(conta)
 
        elif opcao == "d":
            cpf = input("Digite seu cpf (necessario ter conta): ")
            encontrar_conta = verificar_conta(cpf)

            if encontrar_conta == None:
                print("Conta nao encontrada")
            else:
                valor_depositar = float(input("Depósito\nDigite um valor a ser depositado: "))
                encontrar_conta.depositar(valor_depositar)
            
        elif opcao == "s":
            cpf = input("Digite seu cpf (necessario ter conta): ")
            encontrar_conta = verificar_conta(cpf)

            if encontrar_conta == None:
                print("Conta nao encontrada")
            else:
                valor_saque = float(input("Saque\nDigite um valor a ser sacado: "))
                encontrar_conta.sacar(valor_saque)

        elif opcao == "e":
            cpf = input("Digite seu cpf (necessario ter conta): ")
            encontrar_conta = verificar_conta(cpf)

            if encontrar_conta == None:
                print("Conta nao encontrada")
            else:
                encontrar_conta.exibir_extrato()
            
        elif opcao == "q":
            break

        else:
            pass

if __name__ == "__main__":
    main()