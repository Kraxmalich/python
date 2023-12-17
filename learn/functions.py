def add(x, y):
    return x + y
print(add(4, 6))

def add(x, y):
    return x + y
print(add('qwe', 'rty'))

def print_smth(name):
    print('Hello', name)
print_smth('Dmitriy')

def print_smth(name = 'Dima'):
    print('Здарова', name)
print_smth() #Если ввести значение, то оно будет использовано в качестве name

#Вывод факториала с помощью функции
def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod
print(fact(5))
#Вычисление факториала с помощью фугкции используя math
import math
f = math.factorial
print(f(4))

#Использование и взаимодействие функций
def main():
    print_smth('Dima')
    usd_rate = 90
    money = 98000
    result = exchange(usd_rate, money)
    print(result)
def print_smth(name):
    print('Hello', name)
def exchange(usd_rate, money):
    result = round(money/usd_rate, 2) #Число 2 отсчитывает кол-во символов после точки
    return result
main()

#Анонимные функции
#Могут содержать только одно выражение и создаются с помощью инструкции lambda
#Не требует инструкции return
sqrt = lambda x: x**0.5
print(sqrt(25))

l = [1, 3, 5, 7, 9]
print(list(map(lambda x: x**3, l))) #Использование map в анонимной функции