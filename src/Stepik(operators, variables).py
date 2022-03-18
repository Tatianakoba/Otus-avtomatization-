#
# x = int(input())
# y = int(input())
# print(x*60 + y)

# X = int(input())
# print(X//60)
# print(X%60)
#
# X = int(input())
# H = int(input())
# M = int(input())
# print((X + M)//60+H)
# print((X + M)%60)

# A = int(input())
# B = int(input())
# H = int(input())
# if A <= H <= B:
#     print('Это нормально')
# elif H < A:
#     print('Недосып')
# elif H > B:
#     print('Пересып')

# n = int(input())
# if n % 4 == 0 and n % 100 != 0:
#     print('Високосный')
# elif n % 400 == 0:
#     print('Високосный')
# else:
#     print('Обычный')

# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c) / 2
# S = (p*(p - a)*(p - b)*(p - c)) ** 0.5
# print(S)


# a = int(input())
# if -15 < a <= 12 or 14 < a < 17 or 19 <= a:
#     print('True')
# else:
#     print('False')

#
# a = float(input())
# b = float(input())
# oper = str(input())
# if oper == '+':
#     print(a + b)
# elif oper == '-':
#     print(a - b)
# elif oper == '*':
#     print(a * b)
# elif oper == '/':
#     if b != 0:
#         print(a / b)
#     else:
#         print('Деление на 0!')
# elif oper == 'mod':
#     if b != 0:
#         print(a % b)
#     else:
#         print('Деление на 0!')
# elif oper == 'pow':
#     print(a ** b)
# elif oper == 'div':
#     if b != 0:
#         print(a // b)
#     else:
#         print('Деление на 0!')
# else:
#     print('Неподдерживаемая операция')

# figure = str(input())
# if figure == 'треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     S = (p*(p - a)*(p - b)*(p - c)) ** 0.5
#     print(S)
# elif figure == 'прямоугольник':
#     a = int(input())
#     b = int(input())
#     S = a*b
#     print(S)
# elif figure ==  'круг':
#     p = 3.14
#     r = int(input())
#     S = p*r**2
#     print(S)

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(a, b, c, sep="\n")
# elif a == b < c:
#     print(c, a, b, sep="\n")
# elif a == b > c:
#     print(a, c, b, sep="\n")
# elif a < b == c:
#     print(b, a, c, sep="\n")
# elif a > b == c:
#     print(a, b, c, sep="\n")
# elif a == c < b:
#     print(b, a, c, sep = "\n")
# elif a == c > b:
#     print(a, b, c, sep="\n")
# elif a > b > c:
#     print(a, c, b, sep="\n")
# elif a > b < c and a > c:
#     print(a, b, c, sep="\n")
# elif a > b < c and a < c:
#     print(c, b, a, sep="\n")
# elif a < b < c:
#     print(c, a, b, sep="\n")
# elif a < b > c and a < c:
#     print(b, a, c, sep="\n")
# elif a < b > c and a > c:
#     print(b, c, a, sep="\n")

#
# Если вторая с конца цифра 1, то всегда -ов
#
# Иначе если последняя цифра 0, 5-9, то -ов;
# если 1, то -ст; если 2-4, то -ста
#
# Получить вторую с конца цифру: (n % 100) // 10
#
# Получить последнюю: n % 10

# s = int (input())
# n1 =" программистов"
# n2 =" программист"
# n3 =" программиста"
# if  s>=0:
#   if s==0:
#     print(str(s) + n1)
#   elif s%100>=10 and s%100<=20:
#     print(str(s) + n1)
#   elif s%10==1:
#     print(str(s) + n2)
#   elif s%10>=2 and s%10<=4:
#     print(str(s) + n3)
#   else:
#     print(str(s) + n1)

# s = str(input())
# a = int(s[0])
# b = int(s[1])
# c = int(s[2])
# d = int(s[3])
# e = int(s[4])
# f = int(s[5])
# if a+b+c == d+e+f:
#     print('Счастливый')
# else:
#     print('Обычный')
#

