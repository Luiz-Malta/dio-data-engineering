#Lidando com data, hora e fuso horário

import datetime

data = datetime.date(2024, 8, 20) #lançando a data

print(data) #imprimindo a data

print(datetime.date.today())#imprimindo data pelo datetime direto

data_hora = datetime.datetime(2024, 8, 20, 11, 47, 30) #criando a variável data com hora

print(data_hora) #imprimindo data com hora
print(datetime.datetime.today()) # imprimindo data com hora direto pelo datetime

hora = datetime.time(11, 50, 30)
print(hora)

#PT 2 - manipulando data com timedata

#adicionando uma semana em uma data

data = data + datetime.timedelta(weeks=1)

print(data)

#PT 3 - Formatando e convertendo datas com strftime e strptime

#Formatando data e hora
print(data.strftime("%d/%m/%Y %H:%M"))

#Convertendo string para datetime
date_string = "21/08/2024 13:30"
data_string = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")

print(data_string)

#PT 4 - Trabalhando com UTC

import pytz

#criando datetime com timezone

data = datetime.datetime.now(pytz.timezone("Europe/Oslo")) #Criando um objeto com data e hora atual configurado para o horário de Oslo

print(data)


"""Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas
operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3
operações: depósito, saque e extrato.
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha
saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
"""
#import re
from time import sleep
menu = " [d] Depositar \n [s] Sacar \n [e] Extrato \n [q] Sair \n =>"
print(menu)
saldo = 0
limite = 500
numero_saques = 3
LIMITE_SAQUES = 3
with open("Extrato.txt", "w") as extrato:
    extrato.write(f"{'-'*10}EXTRATO CONTA{'-'*10}")

while True:

    opcao = input(menu)

    if opcao =="d":
        print("Depósito")
        valor_deposito = float(input("Insira o valor a ser depositado:"))
        saldo += valor_deposito
        print(f"Você depositou {valor_deposito}, seu novo saldo é {saldo}.")
        with open("Extrato.txt", "a") as extrato:
            extrato.write(f" \n (+) Depositou: {valor_deposito} \n (=) Saldo: {saldo}")
        #extrato.get()

    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Insira o valor a ser sacado:"))
        if valor_saque > limite:
            print("Não é possível realizar essa operação! O valor a ser sacado ultrapassa o limite de valor por saque!")

        elif valor_saque > saldo:
            print("Não é possível realizar essa operação! O valor a ser sacado ultrapassa o saldo da conta!")

        else:
            numero_saques -= 1
            if numero_saques < 0:
                print('Não é possível realizar essa operação! Limite de saques diários atingido!')
            else:
                saldo -= valor_saque
                print(f"Você sacou {valor_saque}, seu novo saldo é {saldo}.")
                with open("Extrato.txt", "a") as extrato:
                    extrato.write(f" \n (-) Sacou: {valor_saque} \n (=) Saldo")

    elif opcao == "e":
        print("Extrato")
        with open("Extrato.txt", "r") as extrato:
            impressao_extrato = extrato.read()
            print(impressao_extrato)

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, tente novamente!")

    sleep(3)
