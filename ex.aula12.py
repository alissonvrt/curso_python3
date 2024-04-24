#Calculo de IMC
print('='*30)
nome = input('Qual seu nome ? ')
peso = input('Qual seu peso ? ')
altura = input('qual sua altura ? ')

con1 = int(peso) #Conversão para inteiros
con2 = float(altura)
imc = con1 / (con2 * con2)

print(f'{nome} tem {altura}m de altura')
print(f'pesa {peso} quilos e seu IMC é {imc:.2f}')
print('='*30)