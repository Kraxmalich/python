#Boolean type - Логические переменные
Name = False
print(Name)
print(type(Name)) #'bool'

#Numeric type - Числа
Name = 22
print(Name)
print(type(Name)) #'int'

Name = 22.3
print(Name)
print(type(Name)) #'float'

Name = 2+3j
print(Name)
print(type(Name)) #'complex'

#Text secuence type - Строки
Name = 'Дима'
print(Name)
print(type(Name)) #'str'

#Binary secuence types - Бинарные Списки
Name = b'bytes' 
print(Name)
print(type(Name)) #'bytes'

Name = bytes([50,100,76,72,41])
print(chr(50))
print(type(Name)) #'bytes'

#Secuence type - Списки
Name = list('список')
print(Name)
print(type(Name)) #'list'

Name = tuple('Привет мир')
print(Name)
print(type(Name)) #'tuple'

#Set types - Множества
Name = set('Привет')
print(Name)
print(type(Name)) #set

Name = frozenset('Привет')
print(Name)
print(type(Name)) #frozenset

#Mapping types - Словари
d = {'Первый':1, 'Второй':2}
print(d)
print(type(d)) #'dict'

d = dict(Первый = 'x', Второй = '1')
print(d)
print(type(d))#'dict'

#Преобразование значений
a = '5'
b = 2
print(int(a) + b) #целочисленное число
print(float(a) + b) #с плавающей точкой число