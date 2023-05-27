"""
enumerate - enumera iteráveis (ínidices)
"""
lista = ['Maria','Helena','Luiz']
lista.append('João')

#lista_enumerada = list(enumerate(lista, start=19))
#print(lista_enumerada)
#print(next(lista_enumerada))

#for item in lista_enumerada:
#   print(item)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
