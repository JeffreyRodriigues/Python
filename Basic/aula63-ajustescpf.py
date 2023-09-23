"""
Calculo do segundo digito do CPF
746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.: 746.824.890-70 (746824890)
	11	10	9	8	7	6	5	4	3	2
 *	7	4	6	8	2	4	8	9	0	7 <-- PRIMEIRO DIGITO
	77	40	54	64	14	24	40	36	0	14
 
 Somar todos os resultado:
 77+40+54+64+14+24+40+36+0+14 = 363
 Multiplicar o resultado anterior por 10
 363 * 10 = 3630
 Obter o resto da divisão da conta anterior por 11
 3630 % 11 = 0
 Se o resultado anterior for maior que 9:
	resultado é 0
 contrário disso:
	resultado é o valor da conta
 
 O segundo digito do CPF é 0
"""
import re
import sys

# cpf = '746.824.890-70' \
#     .replace('.', '') \
#     .replace('-', '') \
#     .replace(' ', '') 
entrada = input('CPF [746.824.890-70]: ')
cpf = re.sub (
    r'[^0-9]',
    '',
    entrada
    ) 

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()
    
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == novo_cpf:
    print(f'{novo_cpf} é válido')
else:
    print('CPF inválido')