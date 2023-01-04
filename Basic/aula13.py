nome = 'Jeffrey Rodrigues'
altura = 1.80
peso = 85
imc = peso / (altura * altura)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa, {peso} quilos, e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

if imc < 18.5:
    print("IMC Abaixo do Normal")
elif imc <= 24.9:
    print('IMC Normal')
elif imc <= 29.9:
    print('IMC Sobrepeso')
elif imc <= 39.9:
    print('IMC Obesidade')
else:
    print('IMC acima do Obesidade')
