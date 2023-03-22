number = int(input('Digite un número: '))
#OPERACIONES RELACIONALES O DE COMPARACIÓN
#True(1)/False(0)
print(number > 3)  #pregusnta sí number es mayor que 3
print(number >= 3)  # pregunta sí number es mayor o igual que 3
print(number < 3)  #pregusnta sí number es menor que 3
print(number <= 3)  # pregunta sí number es menor o igual que 3
print(number == 3)  # pregunta sí number es igual que 3
print(number != 3)  # pregunta sí number es diferente a 3

#OPERACIONES LÓGICAS

print("Operaciones lógicas.")
#Conjunción (AND, &)
print(True and True)
print((number >= 3) and True)
print(False and True)
print((number >= 3) and False)
print(False and False)
print(number >= 3 and False)
print(False and False and True)
print(number >= 3 and False and True)
print(False & False & True)

#Disyunción (or, |)
print("Disyunción:")
print(False or False)
print(False or True)
print(True or False)
print(True or True)
print(number > 3 or True)
print(number > 3 or number < 10)
print(number < 3 or number >= 10)

#Negación (not,~)
print('Negación:')
print(True)
print(not (True))
print(~ False)

#Or exclusiva (^)
print('Or exclusiva:')
print(False ^ False)
print(False ^ True)
print(True ^ False)
print(True ^ True)

#Operaciones de pertenencia o contenido
# in
print('Operador variable in:')
nombre = 'Melissa Cuastuza'
print('C' in nombre)
print('w' in nombre)
