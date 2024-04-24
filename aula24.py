# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
#nome = 'Otávio'
# impressão(nome[2])
# impressão(nome[-4])
# print('vio' em nome)
# print('zero' em nome)
# impressão(10 * '-')
# print('vio' não no nome)
# print('zero' não no nome)

nome = input('Digite seu nome: ' )
encontrar = input('Digite o que deseja encontrar: ' )

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')