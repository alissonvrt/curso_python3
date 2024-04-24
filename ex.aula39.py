#interando strings com while

nome = input("Digite seu nome: ")

indice = 0

nova_string = ''


while indice < len(nome):
    letra = nome[indice]
    nova_string += f'*{letra}'
    indice += 1
    
nova_string += '*'
print(nova_string)
