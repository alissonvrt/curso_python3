"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

qual_seu_nome = input('Qual seu primeiro nome ? ')

caractere = len(qual_seu_nome)

if caractere <= 4:
    print('Seu nome é curto')
    print(f'Seu nome tem {caractere} caracteres')
elif caractere <= 5:
    print('Seu nome é normal')
    print(f'Seu nome tem {caractere} caracteres')
elif caractere > 6:
    print('Seu nome é muito grande!')
    print(f'Seu nome tem {caractere} caracteres')
else:
    print('Você não digitou nenhum nome')
