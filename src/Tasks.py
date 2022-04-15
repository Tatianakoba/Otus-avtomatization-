'''Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.'''


res = {}
for _ in range(int(input())):
    n1, r1, n2, r2 = (int(i) if i.isdigit() else i for i in input().split(';'))
    res[n1] = list(map(sum, zip([1, r1 > r2, r1 == r2, r1 < r2], res.get(n1, [0, 0, 0, 0]))))
    res[n2] = list(map(sum, zip([1, r2 > r1, r2 == r1, r2 < r1], res.get(n2, [0, 0, 0, 0]))))

print('\n'.join(f'{k}: {" ".join(map(str, v))} {v[1] * 3 + v[2]}' for k, v in res.items()))
