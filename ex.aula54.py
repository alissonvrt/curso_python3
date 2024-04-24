#lista de compras com while
import os

lista_vazia = [ ]

#loop while para inserir, apagar e mostra a lista de compras 
while True:
#opções de escolha
    opcoes_de_escolha = input('Selecione uma Opção\n'
    '[i]nserir' '[a]pagar' '[l]istar: ' )

# ser o comprimento da strings for igual a 1 ou opção de escolha for igual a int!
    if len(opcoes_de_escolha) > 1 or opcoes_de_escolha == int:
        print('Essa Opção não está no sistema!!')

    if opcoes_de_escolha == 'i':
        os.system('cls')
        lista_vazia.append(input('Informer o nome do item: '))
        
    if opcoes_de_escolha == 'a':
        escolha = input('Escolha um indice para apagar: ')

        try:
            indice = int(escolha)
            del lista_vazia[indice]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido!')
      
    if opcoes_de_escolha == 'l':
        os.system('cls')

        if len(lista_vazia) == 0:
            print('Nada para listar')

        for item in enumerate(lista_vazia):
            indice, produto = item
            print(indice, produto)