"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
"""
import decimal

numero_1 = decimal.Decimal(0.1) #Caso esteja trabalhando com muitos números após a vírgula !!!UTILIZAR STRING
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 10))