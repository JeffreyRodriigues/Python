nome = 'Jeffrey Rodrigues'
altura = 1.80
peso = 25
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos, e seu IMC é')
print(imc)

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
