nome = input(' Qual é seu nome ? ')
sobrenome = input('Qual seu sobrenome ? ')
idade = input('Qual sua idade ? ')
altura =float(input('Qual sua altura ? '))

conv = int(idade)
ano_nascimento = 2023 - conv

maior_idade = conv >= 18
print('='*25)
print(f'Olá, {nome} de {sobrenome}')
print(f'Aqui está sua ficha tecnica, {nome}!!')
print(f'Nome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Ano de nascimento: {ano_nascimento}')
print(f'É maior de idade ? {maior_idade}')
print(f'Altura em metros: {altura}')
