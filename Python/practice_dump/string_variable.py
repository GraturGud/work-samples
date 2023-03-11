# На вход программе подается одна строка. 
# Напишите программу, которая выводит элементы строки с индексами 0, 2, 4, ... в столбик.
s = input()
for i in range(0, len(s), 2):
    print(s[i])

# На вход программе подается одна строка. 
# Напишите программу, которая выводит в столбик элементы строки в обратном порядке.
# без [::-1]
s = input()
for i in range(len(s) - 1, -1, -1):
    print(s[i])

# На вход программе подаются три строки: имя, фамилия и отчество. 
# Напишите программу, которая выводит инициалы человека.
a, b, c = input(), input(), input()
print(b[0] + a[0] + c[0])

# На вход программе подается одна строка состоящая из цифр. 
# Напишите программу, которая считает сумму цифр данной строки.
n = input()
sum = 0
for i in range(0, len(n)):
    sum += int(n[i])
print(sum)

# На вход программе подается одна строка. Напишите программу, 
# которая выводит сообщение «Цифра» (без кавычек), если строка содержит цифру. 
# В противном случае вывести сообщение «Цифр нет» (без кавычек).
text = input()
for i in range(0, len(text)):
    if text[i] in '1234567890':
        print('Цифра')
        break
else:
    print('Цифр нет')

# На вход программе подается одна строка. 
# Напишите программу, которая определяет сколько раз в строке встречаются символы + и *.
text = input()
count_t = 0
count_p = 0
for i in range(0, len(text)):
    if text[i] == '+':
        count_p += 1
    elif text[i] == '*':
        count_t += 1
print(f'Символ + встречается {count_p} раз', f'Символ * встречается {count_t} раз', sep='\n')

# На вход программе подается одна строка. 
# Напишите программу, которая определяет сколько в ней одинаковых соседних символов.
text = input()
count = 0
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
print(count)

# На вход программе подается одна строка с буквами русского языка. 
# Напишите программу, которая определяет количество гласных и согласных букв.
text = input()
glas_c = 0
sogl_c = 0
for i in range(len(text)):
    if text[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        glas_c += 1
    if text[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        sogl_c += 1
print(f'Количество гласных букв равно {glas_c}', f'Количество согласных букв равно {sogl_c}', sep='\n')

# На вход программе подается натуральное число, записанное в десятичной системе счисления. 
# Напишите программу, которая переводит данное число в двоичную систему счисления.
# Без format()
num = int(input())
mech = ''
while num != 0:
    if num % 2 == 0:
        mech = '0' + mech
    else:
        mech = '1' + mech
    if num // 2 == 0:
        break
    num //= 2
print(mech)