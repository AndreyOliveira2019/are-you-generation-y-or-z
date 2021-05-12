numero1 = 2021
numero2 = int(input('digite seu ano de nascimento: '))
resultado = numero1 - numero2
print('ano atual: ', numero1)
print('seu ano de nascimento: ', numero2)
print('sua idade é: ', resultado)
if resultado < 22:
  print('Você faz parte da geração Z')
else: 
  print('Você faz parte da geração Y')
