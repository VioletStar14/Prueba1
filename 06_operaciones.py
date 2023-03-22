#OPERACIONES ARITMÉTICAS
#SUMA +, RESTA -, MULTIPLICACIÓN *, DIVISIÓN /, DIVISIÓN ENTERA //, MÓDULO ó RESIDUO %, POTENCIA **

number = int(input('Digite un número: '))
print(f'La suma con 2 es: {number+2}')
print(f'La resta con 2 es: {number-2}')
print(f'La multiplicación con 2 es: {number*2}')
print(f'La división con 2 es: {number/2}')
print(f'La división entera con 2 es: {number//2}')
print(f'El residuo con 2 es: {number%2}')
print(f'La potencia con 2 es: {number**2}')


#OPERACIONES DE ASIGNACIÓN
contador = 1
print(f'Antes de la operación += es: {contador}')
contador += 1  #contador = contador +1 (+= operador de asignación incremental)
print(f'Después de la operación += es: {contador}')

number = int(input('Digite un número: '))
number += 1
print(f'Al usar operador incremental += el resultado es: {number}')
number -= 1
print(f'Al usar operador decremental -= el resultado es: {number}')
number *= 2
print(f'Al usar operador *= el resultado es: {number}')
number /= 2
print(f'Al usar operador /= el resultado es: {number}')
number //= 2
print(f'Al usar operador //= el resultado es: {number}')
number %= 2
print(f'Al usar operador %= el resultado es: {number}')
number **= 2
print(f'Al usar operador **= el resultado es: {number}')
