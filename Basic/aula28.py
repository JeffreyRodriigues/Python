"""
Exercício
Peça ao usuário para digitar o seu nome
Peça ao usuário para digitar sua idade
se o nome e idade forem digitados:
	Exiba
		Seu nome é {nome}
		Seu nome invertido é {nome invertido}
		Seu nome contém (ou não) espaços
		Seu nome tem {n} letras
		A primeira letra do seu nome é {letra}
		a última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
	exiba "Desculpe, você deixou os campos vazios
"""
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0:1]}')
    print(f'a última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou os campos vazios")