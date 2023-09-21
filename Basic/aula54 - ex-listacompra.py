"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar, listar valores da sua lista
Não permita que o programa quebre com
erros de indíce inexistentes na lista
"""

import os


lista = []
while True:
    print(u"Selecione uma opção: ")
    opcao = input("[i]nserir [a]pagar [l]istar: ")
    
    if opcao == 'i':
        os.system('clear')
        valor = input("Valor: ")
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(u"Escolha o índice para apagar: ")

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print(u"Por favor, digite um número inteiro")
        except IndexError:
            print(u"Índice não existe na lista")
            
    elif opcao == 'l':
        os.system('clear')
        
        if len(lista) == 0:
            print(u"Nada para listar")
            
        for i, valor in enumerate(lista):
            print(i, valor)