# username = input('Введите Ваше имя')
# age = input('Введите Ваш возраст')
# print(f"Hello, {username}. You are {age} years old."
#
# '''print("My name is {name}, I'm {age}".format(name = "Natalia", age = 22))
# # My name is Natalia, I'm 22
#
# print("My name is {0}, I'm {1}".format("Maria", 25))
# # My name is Maria, I'm 25
#
# print("My name is {}, I'm {}".format("Juiia", 36))
# # My name is Juiia, I'm 36
# ''')

# text = input()
# a = text.replace("'", "\\'").replace('"', '\\"')
# print(a)

# text = input()
# a = text[0:4]
# b = text[4:]
# print(a, b)
'''На вход подаются два числа. Напишите программу, которая их сравнивает.

Если первое число больше второго, выведите True, иначе выведите False. Если числа равны, выведите False.'''
# first, second = input().split()
# first = float(first)
# second = float(second)
# print(first > second)


a, b = map(int, input().split())
print(a%10==0 or b%10==0)
