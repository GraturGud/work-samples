# Напишите программу, которая считывает целое положительное число [ 1 ; 9 ] 
# и выводит значение числа n + nn + nnn
n = int(input())
print(n + (n * 10 + n) + (n * 100 + n * 10 + n))

# Напишите программу, которая считывает четыре целых положительных числа 
# d и выводит на экран значение выражения a**b + c**d

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b + c**d)

# Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы и сумму квадратов этих чисел
a = int(input())
b = int(input())
print(f'Квадрат суммы {a} и {b} равен {(a + b)**2}', f'Сумма квадратов {a} и {b} равна {a**2 + b**2}', sep='\n')

# Напишите программу, которая выводит прямоугольник, по периметру состоящий из звездочек (*)
print('*****************','*               *', '*               *', '*****************', sep='\n')