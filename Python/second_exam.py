# Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. 
# Если год оканчивается, то выведите «YES», иначе выведите «NO»
a = int(input())
if a % 10 == 0 and a % 100 == 0:
    print('YES')
else:
    print('NO')

# Заданы две клетки шахматной доски. 
# Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет. 
# Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO»
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

# Футбольная команда набирает девочек от 10 до 15 лет включительно. 
# Напишите программу, которая запрашивает возраст и пол претендента, 
# используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина) и определяет подходит ли претендент для вступления в команду или нет. 
# Если претендент подходит, то выведите «YES», иначе выведите «NO»
age, gender = int(input()), input()
if 10 <= age <= 15 and gender == 'f':
    print('YES')
else:
    print('NO')

# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. 
# Если число находится вне диапазона 1-10, то программа должна вывести текст «ошибка»
n = int(input())
if n == 1:
    print('I')
elif n == 2:
    print('II')
elif n == 3:
    print('III')
elif n == 4:
    print('IV')
elif n == 5:
    print('V')
elif n == 6:
    print('VI')
elif n == 7:
    print('VII')
elif n == 8:
    print('VIII')
elif n == 9:
    print('IX')
elif n == 10:
    print('X')
else:
    print('ошибка')

# Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
# Условия:
# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».
a = int(input())
if a % 2 != 0 or (a % 2 == 0 and 6 <= a <= 20):
    print('YES')
else:
    print('NO')

# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, 
# может ли слон попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», 
# если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2:
    print('YES')
else:
    print('NO')

# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, 
# может ли конь попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», 
# если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1-y2) == 2):
    print('YES')
else:
    print('NO')

# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, 
# может ли ферзь попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», 
# если из первой клетки ходом ферзя можно попасть во вторую или «NO» в противном случае
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2) or (abs(x1-x2) == abs(y1-y2)):
    print('YES')
else:
    print('NO')