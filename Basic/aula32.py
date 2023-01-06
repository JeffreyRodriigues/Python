"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informq que não é um número inteiro
"""
# numero = input('Digite um número inteiro: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_texto = (par_impar and "par" or "impar")

#     print(f'O número {numero_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

# print('-----------------------------------')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Digite uma hora em números inteiros: ')

# try:
#     hora = int(entrada)
#     DIA = hora >= 0 and hora <= 11
#     TARDE = hora > 11 and hora <= 17
#     NOITE = hora > 17 and hora <= 23

#     if DIA:
#         print('Bom dia')
#     elif TARDE:
#         print('Boa tarde')
#     elif NOITE:
#         print('Boa noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome de usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input('Digite o seu nome: ')
NOME_CURTO = len(nome) >= 1 and len(nome)  <= 4
NOME_NORMAL = len(nome) >= 5 and len(nome) <= 6
NOME_GRANDE = len(nome) >= 7

if NOME_CURTO:
    print(f'Seu nome {nome} é curto, e contém {len(nome)} letras')
elif NOME_NORMAL:
    print(f'Seu nome {nome} é normal, e contém {len(nome)} letras')
elif NOME_GRANDE:
    print(f'Seu nome {nome} é grande, e contém {len(nome)} letras')
else:
    print('Digite mais de uma letra para contabilizarmos o seu nome')
