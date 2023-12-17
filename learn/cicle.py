#Вывод чисел Фибаначи
a, b = 0, 1
while a<10:
    print(a)
    a, b = b, a+b 

#Использование if/else
a = 1
if a == 10:
    print('a = 10')
elif a < 10:
    print('a < 10')
else:
    print('a > 10')

#Использование while (один из самых универсальных циклов)
i = 0
while i < 10: #Пока значение верное, выполняется иттерация
    i += 1
    print(i)

#Вычисление факториала
#n = int(input('Введите число: '))
#i = 1
#fact = 1
#while i <= n:
#    fact *= n
#    i += 1
#print('Факториал равен числу:', fact)

#Использование цикла for
for i in range(2): #Range позволяет повторить результат заданное кол-во раз
    print('Учись')

lst = [1, 3, 5, 7, 9]
for i in lst:
    print(i ** 2)

str = 'Учись'
for i in str:
    print(i)