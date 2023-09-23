"""
Argumentos nomeados e não nomeados em funcções Python
Argumento nomeado não tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)
    
soma(1, 2, 3)
soma(y=2, z=3, x=1)
soma(2, y=3, z=1)