import textwrap

def menu():
    menu = """
    ================ MENU ================
    [1]\t Depositar
    [2]\t Sacar
    [3]\t Extrato
    [4]\t Novo usuario
    [5]\t Nova conta
    [6]\t Listar contas
    [7]\t Listar usuarios
    [0]\t Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, num_saques, limite_saques):
    if num_saques >= limite_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > saldo:
        print("\nOperação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, num_saques

def exibir_extrato(saldo, extrato):
    print("\n=============== EXTRATO ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("========================================")
    
def cadastrar_usuario(usuarios):
    cpf = input("\nInforme o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")
    
    
def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    
    print("\n=============== CONTAS ===============")
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}"""
        print(textwrap.dedent(linha))
    print("=========================================")
        
def listar_usuarios(usuarios):
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return
    
    print("\n=============== USUARIOS ===============")
    for usuario in usuarios:
        linha = f"""\
            Nome: {usuario['nome']}
            Data de Nascimento: {usuario['data_nascimento']}
            CPF: {usuario['cpf']}
            Endereço: {usuario['endereco']}"""
        print(textwrap.dedent(linha))
    print("=========================================")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    limite = 500
    saldo = 0
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            valor = float(input("\nInforme o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("\nInforme o valor do saque: "))
            saldo, extrato, num_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            cadastrar_usuario(usuarios)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "6":
            listar_contas(contas)
            
        elif opcao == "7":
            listar_usuarios(usuarios)
        
        elif opcao == "0":
            print("\nSaindo do sistema...")
            break
        
        else:
            print("\nOpção inválida! Por favor, selecione novamente.")

if __name__ == "__main__":
    main()