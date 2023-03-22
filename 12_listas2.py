num = [99, 34, 25, 56, 72]
print(num)
num[1] = 8
print(num)

#FUNCIÓN INSERT:
#num=[99,88,25,56,72]
num.insert(1, 77)
print(num)

#MÉTODO APPEND():
num.append(object)
#FUNCIÓN APPEND:
num.append(100)
print(num)
#FUNCIÓN EXTEND:
num2 = [9, 8, 7]
num.extend(num2)
print(num)
#FUNCIÓN REMOVE:
num.remove(100)
print(num)
#FUNCIÓN POP:
num.pop(2)
print(num)
#FUNCIÓN DEL:
del num[0]
print(num)
#FUNCIÓN CLEAR:
num2.clear()
print(num2)
