"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#para sabe ser é um número par e só usa o resto da divisão

numero_impar_ou_par = input("Digite um numero inteiro: ")

if numero_impar_ou_par.isdigit():
    numero_inteiro = int(numero_impar_ou_par)
    par_impar = numero_inteiro % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'
else:
    print('você não digitou um número inteiro')

