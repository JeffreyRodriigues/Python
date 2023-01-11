"""
Iterando string com while
"""
#       01234567890123456
nome = 'Jeffrey Rodrigues' #Iteráveis
#       65432109876543210
tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)
