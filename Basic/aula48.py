"""
Listas em Python
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - indíces e fatiamento
"""
#   +01234
#   -54321
# string = 'ABCDE' # 5 caracteres (len)
# lista = [123, True, 'Jeffrey Rodrigues', 1.2, []]
# # print(lista, type(lista))
# lista[-3] = 'Maria'
# print(lista[2])
# print(lista)

"""
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append('BBB')
# ultimo_valor = lista.pop()
# lista.pop(3)
# print(lista, 'Removido,', ultimo_valor)

"""
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
"""

# lista = [10, 20, 30, 40]
# lista.append('Jeffrey')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista clear()
# lista.insert(0, 5)
# print(lista)

"""
    + - concatena listas
"""

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
# print(lista_a)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['João', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)
print(lista_a)
