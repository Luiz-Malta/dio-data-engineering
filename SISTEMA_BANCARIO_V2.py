"""
1)Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas
operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3
operações: depósito, saque e extrato.
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha
saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

2) Separar as opções existentes de saque, depósito e extrato em funções. Criar dias novas funções: cadastrar usuário
(cliente) e cadastrar conta bancária, vinculando a conta ao usuário.

    -> A função de saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo,
    valor, extrato, limite, numero_saques, limite_saques.. Sugestão de retorno: saldo e extrato.

    -> A função de depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos:
    saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

    -> A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).
    Argumentos posicionais: saldo. Argumentos nomeados: extrato.

    -> O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e
    endereço. O endereço é uma string com o formato: logradouro, nro - bairro -cidade/sigla estado. Deve ser armazenado
    somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

    -> O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário.
    O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma
    conta, mas uma conta pertence a somente um usuário.

"""

from time import sleep
import datetime

def menu():
    return print(f"{'-'*15} MENU {'-'*15} \n [d] Depositar \n [s] Sacar \n [e] Extrato "
                 "\n [u] Novo Usuário\n [c] Nova Conta\n [f] Filtra usuário\n [q] Sair \n =>")

def sacar(saldo, valor, limite,limite_saques, extrato):

    if valor > limite:
        print("Seu limite não te permite realizar esse saque! Entre em contato com nosso SAC para mais informações!")
    elif valor > saldo:
        print("Não é possível realizar esse saque pois ele excede seu saldo!")
    elif limite_saques <= 0:
        print("Não é possível realizar mais saques no dia de hoje! ")
    else:
        saldo -= valor
        limite_saques -= 1
        extrato += f'\n(-) R$ {valor}\n(=)R$ {saldo}.'
        print(f"Saque no valor de R$ {valor} realizado! Seu novo saldo é de R$ {saldo}.")

    return saldo, limite_saques, extrato

def depositar(valor, saldo, extrato):
    saldo += valor
    extrato += f'\n(+) R$ {valor}\n(=)R$ {saldo}.'
    print(f'Depósito no valor de R$ {valor} realizado! Seu novo saldo é de R$ {saldo}.')
    return saldo, extrato

def mostrar_extrato(extrato):
    demonstrativo = f"{'='*10} EXTRATO {'='*15} \n{extrato}\n{'-'*40}"
    return print(demonstrativo)

def novo_usuario(nome, nascimento, cpf,endereco,usuarios):
    # Verifica se o CPF já existe entre os usuários cadastrados
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Esse CPF já está cadastrado. Não é possível fazer novo cadastro!")
        return usuarios

    # Adiciona o novo usuário como um dicionário
    usuario = {
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuarios

def nova_conta(agencia, conta, usuarios):
    cpf = input('Insira o CPF da nova conta: ')
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso! ')
        return {"agencia": agencia, "conta": conta, "usuario": usuario}

    else:
        print("Usuário não encontrado!")

def filtra_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def main():
    saldo = 0
    limite = 500
    numero_saques = 3
    limite_saques_global = 3
    operacoes = 0
    usuarios = []
    contas = []
    agencia = '0001'
    extrato = ""
    while True:
        sleep(3)
        menu()

        opcao = str(input()).lower().strip()

        if opcao == 'd':
            valor_deposito = float(input("Insira o valor do depósito(R$): "))
            saldo, extrato = depositar(valor_deposito, saldo, extrato)

        elif opcao == 's':
            valor_saque = float(input("Insira o valor a ser sacado(R$): "))
            saldo, limite_saques_global, extrato =sacar(saldo=saldo,
                                        limite=limite,
                                        limite_saques=limite_saques_global,
                                        valor = valor_saque,
                                        extrato= extrato)

        elif opcao == 'e':
            mostrar_extrato(extrato)

        elif opcao == 'u':
            nome_usuario = input("Insira o nome do usuário: ")
            data_nascimento = ''
            # Tenta converter a data de nascimento em formato datetime
            try:
                data_nascimento = datetime.datetime.strptime(input("Insira a data de nascimento (dd/mm/YYYY): "),
                                                             "%d/%m/%Y")
            except ValueError:
                print("Data de nascimento inválida. Por favor, tente novamente.")
            while True:
                cpf_usuario = input("Insira o CPF do usuário, sem pontuação, apenas números: ")
                if len(cpf_usuario) == 11 and all(digito in '123456789' for digito in cpf_usuario):
                    break
                else:
                    print("CPF Inválido! Tente novamente!")


            # Entrada de dados do endereço
            endereco_usuario = {
                "Logradouro": input("Logradouro: "),
                "Número": input("Número: "),
                "Complemento": input("Complemento: "),
                "Bairro": input("Bairro: "),
                "Cidade": input("Cidade: "),
                "UF": input("UF: "),
                "CEP": input("CEP: ")
            }

            # Chama a função para adicionar o novo usuário
            novo_usuario(nome_usuario, data_nascimento, cpf_usuario, endereco_usuario, usuarios)


        elif opcao == 'c':
            numero_conta = len(contas) + 1
            contas = nova_conta(agencia, numero_conta, usuarios)

        elif opcao == 'f':
            cpf = input("Insira o CPF para verificação")
            filtra_usuario(cpf, usuarios)


        elif opcao == 'q':
            print("Saindo do sistema! \nAgradecemos sua visita!")
            break

        else:
            print('Opção inválida, tente novamente!')
    return opcao


main()
