# Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз
for i in range(10):
    print('Python is awesome!')

# Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз
a, b = input(), int(input())
for i in range(b):
    print(a)

# Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:
# AAA
# AAA
# AAA
# AAA
# AAA
# AAA
# BBBB
# BBBB
# BBBB
# BBBB
# BBBB
# E
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# G
x = 0
for i in range(3):
    x = x + 1
    if x == 1:
        print('AAA\n' * 5 + 'AAA')
    elif x == 2:
        print('BBBB\n' * 5 + 'E')
    elif x == 3:
        print('TTTTT\n' * 9 + 'G')

# На вход программе подается натуральное число n. Напишите программу, которая печатает звездный прямоугольник размерами n × 19
n = int(input())
for i in range(n):
    print('*' * 19)

# Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9, каждая с указанной строкой текста
n = input()
for i in range(10):
    print(i, n)

# На вход программе подается натуральное число n. 
# Напишите программу, которая для каждого из чисел от 0 до n (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек)
n = int(input())
for i in range(n+1):
    print(f'Квадрат числа {i} равен {i**2}')

# На вход программе подается натуральное число n (n≥2) – катет прямоугольного равнобедренного треугольника. 
# Напишите программу, которая выводит звездный треугольник в соответствии с примером
n = int(input())
for i in range(n):
    print('*' * (n-i))

# На вход программе подается три натуральных числа m,p,n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения
# Напишите программу, которая предсказывает размер популяции организмов. Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(f'{i + 1} {m * (p / 100 + 1) ** i}')

# Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все числа от m до n включительно
a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(i)

# Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания, если m<n, или в порядке убывания в противном случае
a, b = int(input()), int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
elif  a> b:
    for i in range(a, b - 1, -1):
        print(i)
else:
    print(a)

# Даны два целых числа m и n (m>n). Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания
a, b = int(input()), int(input())
for i in range(a, b-1, -1):
    if i % 2 != 0:
        print(i)

# Даны два натуральных числа m и n ( m≤n). Напишите программу, которая выводит все числа от m до n включительно удовлетворяющие хотя бы одному из условий:
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.
a, b = int(input()), int(input())
for i in range(a, b + 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)

# Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n
n = int(input())
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')

# На вход программе подаются два целых числа a и b (a≤b). 
# Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно, куб которых оканчивается на 4 или 9
a ,b = int(input()), int(input())
count = 0
for i in range(a, b + 1):
    if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
        count += 1
print(count)

# На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел
number = int(input())
sum = 0
for i in range(number):
    sum += int(input())
print(sum)

# На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения:
# (1 + 1/2 + 1/3 + ... + 1/n) - log(n)
from math import log
n = int(input())
c = 0
for i in range(1, n + 1):
    c += (1 / i)
print(c - log(n))

# На вход программе подается натуральное число n. Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно) квадрат которых оканчивается на 2,5 или 8
n = int(input())
sum = 0
for i in range (1, n + 1):
    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
        sum += i
print(sum)

# На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!
n = int(input())
fac = 1
for i in range(1, n + 1):
    fac *= i
print(fac)

# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел
y = 1
for i in range(10):
    x = int(input())
    if x != 0:
        y *= x
print(y)

# На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей
x = int(input())
count = 0
for i in range(1, x + 1):
    if x % i == 0:
        count += i
print(count)

# На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы
n = int(input())
sum = 0
for i in range(1, n+1):
    if i % 2 != 0:
        sum += i
    else:
        sum -= i
print(sum)

# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке. 
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности
amount = int(input())
max1, max2 = 0, 0
for i in range (amount):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
print(max1, max2, sep='\n')

# Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.
flag = True
for i in range(10):
    x = int(input())
    if x % 2 != 0:
        flag = False
if flag == True:
    print('YES')
else:
    print('NO')

# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи
a = 1
y = 0
for i in range(int(input())):
    b = a
    a = b+y
    y =  b
    print(b, end=' ')

# На вход программе подается последовательность слов, каждое слово на отдельной строке. 
# Концом последовательности является слово «КОНЕЦ» (без кавычек). Напишите программу, которая выводит члены данной последовательности
text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()

# На вход программе подается последовательность слов, каждое слово на отдельной строке. 
# Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). 
# Напишите программу, которая выводит члены данной последовательности.
text = input()
while text != 'КОНЕЦ' and text != 'конец':
    print(text)
    text = input()

# На вход программе подается последовательность слов, каждое слово на отдельной строке. 
# Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). 
# Напишите программу, которая выводит общее количество членов данной последовательности
text = input()
count = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    count += 1
    text = input()
print(count)

# На вход программе подается последовательность целых чисел делящихся на 7, каждое число на отдельной строке. 
# Концом последовательности является любое число не делящееся на 7. 
# Напишите программу, которая выводит члены данной последовательности
x = int(input())
while x % 7 == 0:
    print(x)
    x = int(input())

# На вход программе подается последовательность целых чисел, каждое число на отдельной строке. 
# Концом последовательности является любое отрицательное число. 
# Напишите программу, которая выводит сумму всех членов данной последовательности.
x = int(input())
sum = 0
while x >= 0:
    sum += x
    x = int(input())
print(sum)

# На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на отдельной строке. 
# Концом последовательности является любое отрицательное число, либо число большее 5. 
# Напишите программу, которая выводит количество пятерок
x = int(input())
count = 0
while 0 <= x <= 5:
    if x == 5:
        count += 1
    x = int(input())
print(count)

# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, 
# к тому же ведьмак не принимает купюры, он принимает только чеканные монеты. 
# В мире ведьмака существуют монеты с номиналами 1,5,10,25. 
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
price = int(input())
count = 0
while price >= 25:
    price -= 25
    count += 1
while price >= 10:
    price -= 10
    count += 1
while price >= 5:
    price -= 5
    count += 1
while price >= 1:
    price -= 1
    count += 1
print(count)

# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке
num = int(input())
while num != 0:
    print(num % 10)
    num //= 10

# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный
num = int(input())
while num != 0:
    print(num % 10, end='')
    num //= 10

# Дано натуральное число n,(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры
num = int(input())
max_n = -1
min_n = 10
while num != 0:
    if num % 10 > max_n:
        max_n = num % 10
    if num % 10 < min_n:
        min_n = num % 10
    num = num // 10
print(f'Максимальная цифра равна {max_n}', f'Минимальная цифра равна {min_n}', sep='\n')

# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры
n = int(input())
counter = 0
total = 0
product = 1
frst = n // 10**(len(str(n)) - 1)
lassst = n % 10
while n != 0:
    last = n % 10
    counter += last
    total += 1
    product *= last
    n //= 10
print(counter, total, product, counter / total, frst, frst + lassst, sep = '\n')

# Дано натуральное число n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
n = int(input())
while n > 9:
    i = n % 10
    if len(str(n)) == 2:
        print(i)
    n //= 10

# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
flag_same = True
num = int(input())
n1 = num % 10
while num !=0:
    n2 = num % 10
    if n1 != n2:
        flag_same = False
    num //= 10
if flag_same == True:
    print('YES')
else:
    print('NO')

# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию
n = int(input())
flag = True
while n // 10 > 0:
    n1 = n % 10
    n2 = (n // 10) % 10
    if n2 < n1:
        flag = False
    n //= 10
if flag == True: 
    print('YES')
else:
    print('NO')

# На вход программе подается число n>1. Напишите программу, которая выводит его наименьший отличный от 1 делитель
n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break

# На вход программе подается натуральное число n. Напишите программу, которая выводит числа от 1 до n включительно за исключением:
# чисел от 5 до 9 включительно;
# чисел от 17 до 37 включительно;
# чисел от 78 до 87 включительно.
n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)

# Дано натуральное число n (n≤ 9). 
# Напишите программу, которая печатает таблицу размером n×3 состоящую из данного числа (числа отделены одним пробелом).
n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()

# Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×5, 
# где в i-ой строке указано число i (числа отделены одним пробелом).
n = int(input())
for i in range(1, n + 1):
    for j in range(5):
        print(i, end=' ')
    print()

# Дано натуральное число n (n≤ 9). Напишите программу, 
# которая печатает таблицу сложения для всех чисел от 1 до n в соответствии с примером.
num = int(input())
for i in range(1, num + 1):
    for j in range(1, 10):
        print(f'{i} + {j} = {i + j}')
    print()

# Дано нечетное натуральное число n. Напишите программу, 
# которая печатает равнобедренный звездный треугольник с основанием, равным n в соответствии с примером:
# *
# **
# ***
# ****
# ***
# **
# *
n = int(input())
middle = n // 2 + 1
for i in range(1, middle +1):
    print('*' * i)
for i in range(middle-1,0,-1):
    print('*' * i)

# Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:
# 1
# 22
# 333
# 4444
# 55555
# ...
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(str(i), end='')
    print()

# Дано натуральное число n. Напишите программу, 
# которая печатает численный треугольник с высотой равной n, в соответствии с примером:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...
n = int(input())
count = 1
for i in range(1, n + 1):
    for j in range(i):
        print(count, end=' ')
        count += 1
    print()

# Дано натуральное число n. Напишите программу, 
# которая печатает численный треугольник с высотой равной n, в соответствии с примером:
# 1
# 121
# 12321
# 1234321
# 123454321
# ...
num_lines = int(input())
for lines in range(1, num_lines + 1):
    for row_asc in range(lines):
        print(row_asc + 1, end='')
    for row_desc in range(lines - 1, 0, -1):
        print(row_desc, end='')
    print()

# На вход программе подается два натуральных числа a и b (a< b). 
# Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей
a = int(input())
b = int(input())
number = 0
sum_ = 0
max_sum = 0
max_number = 0
for i in range(a, b+1):
    for j in range(1,i+1):
        if i % j == 0:
            number = i
            sum_ += j
    if max_sum <= sum_:
        max_number = number
        max_sum = sum_
    sum_ = 0
print(max_number, max_sum)

# На вход программе подается натуральное число n. 
# Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно. 
# В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.
n = int(input())
for lines in range(1, n + 1):
    print(lines, end='')
    for row in range(1, lines + 1):
        if lines % row == 0:
            print('+', end='')
    print()

# На вход программе подается натуральное число n. 
# Напишите программу, которая находит цифровой корень данного числа. 
# Цифровой корень числа n получается следующим образом: если сложить все цифры этого числа, 
# затем все цифры найденной суммы и повторить этот процесс, 
# то в результате будет получено однозначное число (цифра), которое и называется цифровым корнем данного числа.
n = int(input())
while n >= 10:
    temp_n = n % 10
    n //=10
    n += temp_n
print(n)

# Дано натуральное число n. Напишите программу, которая выводит значение суммы 1!+2!+3!+…+n!
from math import factorial
n = int(input())
sum_f = 0
for i in range(1, n+1):
    sum_f += factorial(i)
print(sum_f)

# На вход программе подается два натуральных числа a и b (a< b). 
# Напишите программу, которая находит все простые числа от a до b включительно
a, b = int(input()), int(input())
for i in range(a, b + 1):
    if i <= 1:
        continue
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += 1
    if total == 2:
        print(i)