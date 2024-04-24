# Exercicios
# Crie funções que duplicam, triplicam e quadruplicam 
# o número recebido como parâmetro


def numeros_recebidos(numero):
    def numeros_inseridos():
        return f'{(((numero*numero)*numero)*numero)*numero}'
    return numeros_inseridos

numeros = numeros_recebidos(int(input('digite um numero: ')))



print(numeros())


def criar_multiplicador(mutiplicador):
    def multiplicar(numero):
        return numero * mutiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quaduplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quaduplicar(2))