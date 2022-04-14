# def f(n):
#     return n * 10 + 5
#
# print(f(f(f(10))))
# print(min(5,3))

# print(min([2,5,1,5,3]))
'''Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

f(x)= \begin{cases}   1 - (x + 2)^2,\quad &\text{при } x\le -2\\  -\frac x2 ,\quad &\text{при } -2 \lt x \le 2\\   (x-2)^2 + 1,\quad &\text{при } 2 \lt x \end{cases}
f(x)=
⎩
⎨
⎧
​

 1−(x+2)
2
 ,
 −
2
x
​
 ,
 (x−2)
2
 +1,
​

при x≤−2
при −2<x≤2
при 2<x
​

Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

'''
# def Her_func(x):
#     float(x)
#     if x <= -2:
#         return 1-((x + 2) ** 2)
#     if -2 < x <= 2:
#         return -(x/2)
#     if 2 < x:
#         return ((x-2)**2)+1
#
# print(Her_func(4.5))

'''Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка'''


# def modify_list(l):
#     for i in range(len(l)-1,-1, -1):
#         if l[i] % 2 == 1:
#             l.pop(i)
#     for i in l:
#         if i % 2 == 0:
#            l[l.index(i)] = l[l.index(i)] // 2
#
# lst = [1, 2, 3, 3, 5, 4, 5, 7, 6 ]
# modify_list(lst)
# print(lst)

'''Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.

Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key нет, то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].

Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}'''
# d = {}
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif 2 * key in d:
#         d[2 * key] += [value]
#     else:
#         d[2 * key] = [value]

'''Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.'''
# s = str(input()) # Ввод строки
# sp = s.lower().split() # Разделяем слова
# d = {}
# for i in sp:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
#
#

#
# for j in d:
#     print(j,d[j])
'''d = dict.fromkeys(sp) #Перевод списка в словарь'''

'''Вариант 2. Списки'''

# s = str(input()) # Ввод строки
# sp = s.lower().split() # Разделяем слова
# y = []
# for i in sp:
#     if i not in y:
#         y.append(i)
#         print(i, sp.count(i))
#     else:
#         pass

'''Напишите программу, которая считывает строку с числом nn, которое задаёт количество чисел, которые нужно считать. Далее
считывает nn строк с числами x_ix 
i , по одному числу в каждой строке. Итого будет n+1n+1 строк.

При считывании числа x_ix 
i  программа должна на отдельной строке вывести значение f(x_i)f(x 
i ). Функция f(x) уже реализована и доступна для вызова. 

Функция вычисляется достаточно долго и зависит только от переданного аргумента xx. Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.'''
#
# d = {}
# n = int(input())
# for i in range(n):
#     x = int(input())
#     if x in d:
#         print(d[x])
#     else:
#         d[x] = f(x)
#         print(d[x])


'''Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.'''
# digits = set('0123456789')
# i = 0
# multiplier = ''
# decrypted = ''
#
# with open('/home/tatianasergey/Загрузки/dataset_3363_2.txt') as in_f_obj:
#     string = in_f_obj.readline().strip()
#
# char = string[i]
# i += 1
#
# while i < len(string):
#
#     while string[i] in digits:
#         multiplier += string[i]
#         i += 1
#         if i > (len(string) - 1):
#             break
#
#     # print(char * int(multiplier), end='')
#     decrypted += (char * int(multiplier))
#
#     multiplier = ''
#     if i > (len(string) - 1):
#         break
#     char = string[i]
#
#     i += 1
#
# with open('/home/tatianasergey/Загрузки/dataset_3363_2.txt', 'w') as out_f_obj:
#     out_f_obj.write(decrypted)


'''Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.'''
# dictionary = {}
#
# with open('/home/tatianasergey/Загрузки/dataset_3363_2.txt') as in_f_obj:
#     for line in in_f_obj:
#         line = line.lower()
#         for word in line.split():
#             if word not in dictionary:
#                 dictionary[word] = 1
#             elif word in dictionary:
#                 dictionary[word] += 1
#
# max_quantity = 1
#
# for key, value in dictionary.items():
#         current_quantity = dictionary[key]
#         if current_quantity > max_quantity:
#                 max_quantity = current_quantity
#                 word_with_max_quantity = key
#
# with open('/home/tatianasergey/Загрузки/dataset_3363_2.txt', 'w') as out_f_obj:
#         most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
#         out_f_obj.write(most_popular)
'''или'''
# with open("/home/tatianasergey/Загрузки/dataset_3363_3.txt", 'r') as f:
#     s = list(map(lambda i: i.strip('.,!?'), f.read().lower().split()))
#     m = max(sorted(s), key = lambda j: s.count(j))
#     print("%s %d" % (m, s.count(m)))
