"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_do_dia = float(input('Que horas é agora ? '))


try:
    if hora_do_dia <= 11:
        print(f'São {hora_do_dia}h Bom dia')
    elif hora_do_dia <= 17:
        print(f'São {hora_do_dia}h Boa tarde')
    elif hora_do_dia <= 23:
        print(f'São {hora_do_dia}h Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
