# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# J e f f r e y
# -6-5-4-3-2-1
# nome = 'Jeffrey'
# print(nome[2])
# print(nome[-1])
# print('fr' in nome)
# print('fr' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
