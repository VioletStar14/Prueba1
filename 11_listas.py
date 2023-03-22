#LISTA
primera_lista = ['Manzana', 'Banano']
print(primera_lista)
nombres = ["Meli", "Cesar", "Lina"]
print(nombres)
cosas = ["Alejo", 14, True, 3.14, 'Meli']
print(cosas)
#LISTA TIPO ENTERO CON FLOTANTE:
Lista1 = [2, 4, 89, 1000, 3.14]
print(Lista1)
#LISTA TIPO LETRA, NUMERO Y BOOLEANO:
Lista2 = ['a', 123, 'A', 3.1416, 'Palabra', True, 1000]
print(Lista2)
#TAMAÑO DE UNA LISTA (LEN):
print('Tamaño de una lista:')
print(len(Lista1))
print(len(Lista2))
#TIPO DE DATO LISTA:
print('Tipo de dato lista:')
print(type(Lista1))
print(type(Lista2))
#OTRA LISTA:
print('Función list():')
num = [1, 2, 3, 4, 5]
print(num)

num2 = list((1, 2, 3, 4, 5))
print(num2)

num2 = list([1, 2, 3, 4, 5])
print(num2)

num2 = list({1, 2, 3, 4, 5})
print(num2)

#LA INDEXACIÓN EN LAS LISTAS:
print('Index list:')
print(num[0])
print(num[0:3])
print(num[-1::-1])
#USO DE LA FUNCIÓN IN:
print('Uso de la Función in:')
print(3 in num)
print(10 in num)
#LA FUNCIÓN Is:
num1 = num
print(num)
print(num1)
print(num2)
print(num1 is num)
print(num2 is num)
