#Condicional If

numero = int(input('Sr. usuario, digite un número: '))
if (numero > 50):
  print('VERDADERO')
else:
  print('FALSO')
  print('La instrucción "If" terminó')

adivinar = 42
numero = int(input('Sr. usuario, digite un número: '))
if (numero > adivinar):
  print('Bájele el volumen')
elif (numero < adivinar):
  print('Súbale el volumen')
else:
  print("verdadero")
  print('La instrucción "If" terminó')
