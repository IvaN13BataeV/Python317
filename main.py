# name = "admin"
# print("Hello", name)
# age = 20.2
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))
# import re
# import json
# import csv

# a = b = c = 3
# print(a, b, c)
# a, b, c = 7, "Hello", 9.2
# print(a, b, c)

# PI = 3.14
# print(PI)
# PI = 2  # нарушение соглашения
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a, b = b, a
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# print("a:", a)  # 2
# print("b:", b)  # 1

# print("строка \n"
#       "символов")
# print('строка символов строка символов строка символов строка символов '
#       'строка символов строка символов строка символов строка символов строка символов ')
# print("\"program\" \rC:\\folder\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3)
# print(s3 * 3)

# print(5146516511616516516516565156165165165165165)
# print(5.146516511616516516516565156165165165165165)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)
# print(5 / 2)
# print(5 // 2)
# print(6 // 2)
# print(6 ** 2)
# print(6 % 2)

# a = 5;
# b = 7;
# c = 3
# print("Сумма:", a + b + c)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", (a + b + c) // 3)

# numbers = 6 + 4 * 5 ** 2 + 7
# print(numbers)
# numbers = (6 + 4) * (5 ** 2 + 7)
# print(numbers)

# num = 10
# num += 5
# print(num)  # 15
#
# num -= 3
# print(num)  # 12
#
# num *= 4
# print(num)  # 48

# num = 4321  # 1234
# res = num % 10 * 1000  # 1000
# num //= 10  # 432
# res += num % 10 * 100  # 200
# num //= 10  # 43
# res += num % 10 * 10  # 30
# num //= 10  # 4
# res += num % 10  #4
# print(res)


# print(int(3.8))  # 3
# a = round(3.84646456, 2)
# print(round(3.84646456))  # 4
# print(a, type(a))

# a = '5.2'
# b = 10
# c = float(a) + b  # в int не преобразует
# print(c)

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.",  end=" ", sep="---")
# print("Hello")

# name = input("Введите имя: ")
# city = input("Введите город: ")
# print(name, city)


# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# one = int(input("1: "))
# two = int(input("2: "))
# three = int(input("3: "))
# four = int(input("4: "))
# res = round(((one + two)/(three + four)), 2)
# print("Результат:", res)

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5
# print(type(b1))

# print(bool("python"))
# print(bool(""))
# print(bool(10))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))

# print(7 == 7)
# print(7 == "7")
# print(2 + 5 == 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 8)
# print("привет" > "ПРИВЕТ")  #  сравнивается код первых букв слов 175 > 143

# print(2 < 4 < 9)  # True : True => True
# print(2 < 4 > 9)  # True : False => False
# print(2 * 5 > 7 >= 4 + 3)  # True
# print(3 * 3 <= 7 >= 2)  # False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and False => True
# print(5 - 3 < 2 or 1 + 3 < 4)  # False or False => False
# print(not 9 - 5)  # False
# print(not 9 - 9)  # True

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# PEP20
# import this

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# first_side = int(input("Введите первую сторону: "))
# second_side = int(input("Введите вторую сторону: "))
# third_side = int(input("Введите третью сторону: "))
# if first_side == second_side == third_side:
#     print("Треугольник равносторонний")
# elif first_side == second_side or second_side == third_side or first_side == third_side:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4 :
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# m = int(input("Введите номер месяца: "))
# if m == 1 or m == 2 or m == 12:
#     print("Зима")
# elif 2 < m < 6:
#     print("Весна")
# elif 5 < m < 9:
#     print("Лето")
# elif 8 < m < 12:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# password = "admin"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")

# day = 'суббота'
# time = 13
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print('Рабочий день')
#     case 'суббота' | 'воскресенье' if 9 <= time <= 12:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# a, b = 30, 20

# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print(a/b if b != 0 else "Деление на ноль невозможно")


# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n/m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки и нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключений
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")

# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
# finally:
#     print(a + b)


# Цикл

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 2

# i = 1
# while i < 21:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Укажите количество символов: "))
# print("*" * n)
# print("+-" * int(n / 2))

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1

# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# 1 - 5 => 1 + 3 + 5 => 9
# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print("Сумма целых нечетных чисел:", res)

# n = input("Введите целое число: ")

# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите число"))
#     if n == 0:
#         break
#     res *= n
# print("Результат:", res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*", sep="")
#     i += 1

# for i in "Hello":
#     print(i)

# for color in "red", "yellow", "green", 1, 20, 0.3:
#     print(color)

# print(range(2, 5, 2))  # range(start, stop, step) числовые значения
# print(range(9))  # start=0, step=1
# for i in range(100, 0, -10):
#     print(i, end=" ")
#
# print()
#
# i = 100
# while i > 0:
#     print(i, end=" ")
#     i -= 10

# n = int(input("Введите целое число: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите ширину прямоугольника: "))
# for i in range(b):
#     for j in range(a):
#         if i == 0 or i == b - 1 or j == 0 or j == a - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print([i * 2 for i in "Python"])
# print([i for i in range(30) if i % 2 == 0])


# Списки (list)

# num = [9, 3, 8, 4, 1, "Hello", 2.3, True]
# print(num)
# print(type(num))
# print(num[0])
# print(num[2])
# print(num[-1])
# print(num[7])
# print(num[8])  # несуществующий индекс списка => IndexError
# num[1] = 100
# num[2] += 50
# num[8] = 2  # несуществующий индекс списка => IndexError
# print(num[len(num) - 1])
# print(num[-1])

# num = []
# print(num)
# print(type(num))


# nums = list(range(9))
# print(nums)
# print(type(nums))

# nums = list("Hello")
# num = nums * 2
# print(num + [1, 2, 3])

# nums = list(range(2, 100, 10))
# print(nums)
#
# for i in range(len(nums)):
#     print(nums[i])

# for i in nums:
#     print(i)

# генератор списков
# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)
# b = [i ** 2 for i in range(1, 6)]
# print(b)
# c = [c * 3 for c in "list"]
# print(c)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("->"))
# print(a)

# a = [input("-> ") for i in range(int(input("n = ")))]
# print(a)

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# s = 0 
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
# # print(s)
# for i in a:
#     if i < 0:
#         s += i
# print(s)

# lst = list(range(10, 100, 10))
# print(lst)
# for i in range(len(lst)):
#     print(lst[i], end=" ")
# print()
# for i in lst:
#     print(i, end=" ")

# colors = ["red", "blue", "green"]
# for i in range(len(colors)):  # 0 1 2
#     print(colors[i], end=" ")
# print()
# for i in colors:
#     print(i, end=" ")

# n = list(range(21, 41))
# print(n)
# count = s = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         count += 1
# #     else:
# #         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i
# print("Количество четных элементов списка:", count)
# print("Сумма нечетных элементов списка:", s)

# n = [4, 9, 6]
# print(n)
# i = 2 
# print(n[i])
# print(n[i - 1])

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)

# for i in range(1, len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")

# a = [7, 9, 3, 1, 2]
# print(a)
# print('[0]', id(a[0]))
# print('[1]', id(a[1]))
# a[0], a[1] = a[1], a[0]
# print(a)
# print('[0]', id(a[0]))
# print('[1]', id(a[1]))


# Срезы - список[start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s, id(s))
# b = s[5:16]
# print(b, id(b))

# s = "Hello World!"
# print(s[6:-1])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2:5] = []
# print(s)
# del s[1:3]
# print(s)

# Методы списков
# dir(list)
# s = [9,3,7,8,4,6,5]
# print(s)
# # s[len(s):] = [12]
# s.append(12)  # Добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # Добавляет любое количество элементов в конец списка
# print(s)
# s.extend("add")
# print(s)
# s.insert(-1, 'Hello')  # Добавляет элемент (второй параметр) в список в заданный индекс (первый параметр)
# print(s)


# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []  # [2,1,4,3]

# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 5]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])

# if len(b) > len(a):
#     for i in range(len(a)):  # работает только при одинаковой длине списков
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# a = [1, 3, 2, 3, 4, 5]
# print(a)
# # n = 2
# # if n in a:
# #     a.remove(n)  # делает удаление по значению, выбрасывает исключение ValueError, если элемента не существует
# last = a.pop()  # удаляет последний элемент из списка и возвращает его
# print(last)
# print(a)
# second = a.pop(1)  # удаляет элемент по заданному индексу (IndexError)
# print(second)
# print(a)
# a.clear()  # очищает список от элементов
# print(a)

# n = [int(input("Введите элемент: ")) for i in range(int(input("Введите число элементов: ")))]
# k = int(input("Введите индекс: "))
# print("k =", k)
# n.pop(k)
# print(n)

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# num = a.count(5)  # возвращает количество заданных значений в списке
# print(num)
# ind = a.index(2)  # возвращает индекс заданного значения
# print(ind)
# a.reverse()  # перестраивает элементы списка в обратном порядке
# print(a)
# a.sort(reverse=True)  # сортировка списка
# print(a)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(key=len)
# print(s)
# print(len("Александр"))

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# # a.sort()
# sorted(a)  # возвращает отсортированный новый список, не изменяет исходный список
# print(a)

# a = [1, 2, 3]
# b = a.copy()  # возвращает копию списка
# print("a =", a, id(a))
# print("b =", b, id(b))
# a.append(20)
# b.append(120)
# print("a =", a, id(a))
# print("b =", b, id(b))

# Генерация случайных данных

# import random

# print(random.random())  # от 0 до 1 (не включая 1)
# print(random.randint(0, 9))  # от 0 до 9 (включительно)
# print(random.randrange(2, 9))  # randrange(start, stop, step)
# print(round(random.uniform(10.5, 25.5), 2))
#
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
#
#
# numbers = [20, 30, 40, 50, 60, 70, 80, 90]
# print(random.choice(numbers))
# print(random.choices(numbers, k=3))
# print(random.shuffle(numbers))
# print(numbers)

# mas = [random.randint(0, 100) for i in range(10)]
# mas = ['a', 'b', 'c']
# print(mas)
# print(len(mas))
# print(min(mas))
# print(max(mas))

# print(sum(mas))

# s = 0
# for i in mas:
#     s += i  # s = s + i
# print(s)

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# m = max(mas)
# print(m)
# mas.remove(m)
# mas.insert(0, m)
# print(mas)

# mas = [random.randint(-20, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# m = min(mas)
# print("Min:", m)
# ind = mas.index(m)
# print("Index min:", ind)
# print(mas[ind:])
# del mas[:ind]
# print(mas)

# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# print(c)

# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений:", c)

# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print(c)

# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
#
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
# print(matrix)
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)
# import random
# count = 0
# w, h = 3, 4
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#
#         if x < 0:
#             count += 1
#     print()
# print("Количество отрицательных чисел:", count)


# Modules

# import math

# print(math.sqrt(4))
# print(math.pi)
# print(math.ceil(3.2))  # 4
# print(math.floor(3.8))  # 3

# import math as m
#
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import ceil, floor
#
# print(ceil(3.2))
# print(floor(3.8))

# from math import *
#
# print(ceil(3.2))
# print(floor(3.8))

# from math import pi
#
# radius = int(input("Введите радиус окружности: "))
# print('Длина окружности:', round(2 * pi * radius, 2))

# from math import sqrt
# a = int(input("Катет 1: "))
# b = int(input("Катет 2: "))
# print("Гипотенуза:", sqrt(a ** 2 + b ** 2))

# import time
# import locale

# locale.setlocale(locale.LC_ALL, "bel")
#
# seconds = time.time()
# print(seconds)
# print(time.ctime())
# print(time.ctime(12538))
# res = time.localtime()
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("Сегодня: %B %d, %Y"))
# print(time.strftime("%B %d, %Y", time.localtime(5395353)))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))

# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "секунд")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)
#
#
# Функции
#
# def hello(name):
#     print("Hello", name)
#
#
# hello("Irina")
# hello("Ivan")


# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
# get_sum('abc', 'def')


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two


# m = maximum(9, 16)
# print(m)

# def raznost(a,b):
#     if a > b:
#         return a - b
#     else:
#         return a + b


# res = raznost(int(input()), int(input()))
# print(res)

# def cube(a):
#     return a * a * a


# for i in range(1,11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst


# print(change([1,2,3]))
# print(change([9,12,33,54,105]))
# print(change(['с', 'л', 'о', 'н']))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False


# print(func(10, 5))
# print(func(5, 10))
# a = 5 
# b = 10 
# if func(a, b):
#     print("Первое число больше второго")
# else: 
#     print("Второе число больше первого")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False

#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True

#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False


# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d


# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))  # 9 
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))  # 8

# def set_param(c=20, s="-"):
#     print(s * c)


# set_param()
# set_param(7)
# set_param(s="#")

# def digit_sum(n, even=True):
#     s = 0 
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s    


# print("Сумма четных цифр:")   
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))

# print("Сумма нечетных цифр:")   
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age, nm):
#     print("Name:", name, "\nAge:", age)
#
#
# # display_info("Ira", 23)
# # display_info(23, "Ira")
# # display_info(age=23, name="Ira")
# display_info(nm="Igor", age=23, name="Ira")

# a = "Hello"
# b = "Hello"
# b = b + "_new"
# print(a, id(a))
# print(b, id(b))
# print(a == b)  # True
# print(a is b)  # True

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)  # True
# print(lst1 is lst2)  # False

# Изменяемые объекты - list
# Неизменяемые объекты - int, float, bool, str, tuple

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))

# Кортежи (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = "red", "blue", "green"
# print(a)
# print(type(a))

# a = (5,)
# print(a)
# print(type(a))

# a = tuple("Hello")
# a = tuple([1, 5, 8, 9, 6])
# print(a)
# print(type(a))
# print(a[0])
# print(a[1:3])
# a[2] = 12
# print(a)

# from random import randint

# s = tuple(i for i in range(5))
# s = tuple(input("-> ") for i in range(5))
# s = tuple(randint(20, 40) for i in range(5))
# print(s)

# t = tuple(2 ** i for i in range(1, 13))
# print(t)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3.count('l'))
# print(t3.count('a'))
# # print(t3.index('l', 4))
# ch = "w"
# try:
#     print(t3.index(ch))
# except ValueError:
#     print("Такого символа в кортеже не существует")
# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # first = tpl.index(el)  # 1
#             # second = tpl.index(el, first + 1)  # 4 + 1
#             # return tpl[first:second + 1]  # [1:5]
#             return tpl[tpl.index(el):tpl.index(el, tpl.index((el) + 1) + 1)]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()


# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def ran(start, end):
#     return tuple(randint(start, end) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
# print(tpl1 + tpl2, (tpl1 + tpl2).count(0))

# t = (10, 11, (1, 2, 3), [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#

# user = get_user()
# first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])

# def func(lst):
#     return sum(lst), len(lst)
#
#
# a, b = func([2, 9, 6, 5, 8, 7, 5, 8, 7, 1, 4, 5, 4])
# print("Сумма:", a)
# print("Количество:", b)

# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst1 = list(tpl)
# print(lst1)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326),("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2),("Марсель", 1.6)))
# )
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


# Множество (set) - неупорядоченная коллекция, которая содержит уникальные элементы

# s = {'banana', 'apple', 'orange', 'banana', 'apple'}
# print(s)
# print(len(s))
# print(type(s))
# for i in s:
#     print(i)

# s = ['banana', 'apple', 'orange', 'banana', 'apple']
# print(s)
# st = set(s)
# print(st)
# s1 = list(st)
# print(s1)

# a = set("Hello")
# print(type(a))
# print(a)

# s = {input("-> ") for i in range(15)}
# print(s)

# a = set("Hello")
# print(a)
# # print('o' in a)
# # print('a' in a)
# a.add("a")
# print(a)
# el = "e"
# if el in a:
#     a.remove(el)  # KeyError
# print(a)
# a.discard("o")
# print(a)
# a.pop()
# print(a)
# a.clear()
# print(a)

# print("Данные для добавления на GitHub")

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = [i for i in s if 'a' not in i]
# # a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c']
# print(a)
# print(['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in ['ab_1', 'ac_2', 'bc_1', 'bc_2'] if i[1] == 'c'])
# тернарное выражение q = True if условие else False
# lst = []
# for i in s:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             lst.append('A' + i[1:])
#         else:
#             lst.append('B' + i[1:])
# print(lst)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a | b # объединение множеств в другое
# c = a & b # пересечение множеств в другом
# c = a - b # разница множеств в другом
# c = a ^ b
# c = a.union(b)
# print(c)
# a |= b  # добавление в текущее множество
# a &= b
# a -= b
# a ^= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))
#
# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)
# # for i in s:
# #     print(i, end=" ")

# a = "Python"
# b = "Programming language"
# print(set(a) - set(b))

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobby = drawing & music
# print(both_hobby)
# drawing -= both_hobby
# print(drawing)


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a < b)

# frozenset - неизменяемое множество

# s = frozenset([1, 2, 3, 4, 5, 6])
# s = frozenset("hello")
# print(s)


# Словари (dict)

# s = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(s[1])
# print(d["two"])
#
# s1 = ["one", "two", "three"]
# d1 = {1: "one", 2: "two", 3: "three"}
# print(s1[1])
# print(d1[2])

# d = {0: "test", "one": 45, (1, 2.3): "Кортеж", True: 1, 35: [2, 3, 6, 7], "one": "один", False: "один"}
# print(d)
# d[(1, 2.3)] = 100
# print(d)

# d = {"one": 1, "two": 2}
# print(d)
# print(type(d))

# d1 = dict(one='one', two=2)
# print(d1)
# print(type(d1))

# d1 = dict([("one", 1), ("two", 2)])
# d1 = dict(["on", ("two", 2)])
# print(d1)

# d = {x: x ** 2 for x in range(7)}
# print(d)

# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# print("two" in d)
# print(len(d))
# for key in d:
#     print(key, "->", d[key])
# key = "six"
# del d[key]
# if key in d:
#     print(d[key])
# try:
#     print(d[key])
# except KeyError:
#     print("Такого ключа не существует")
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
# print(res)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {x: input("-> ") for x in range(1, 5)}
# print(d)
# try:
#     dislike = int(input("Какой элемент исключить: "))
#     del d[dislike]
# except (ValueError, KeyError):
#     print("Такого элемента не существует")
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': [5,6], 'x4': -1}
# print(len(d))

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core-i3-4670K', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core-i5-3450', 5, 6400],
# }

# for key in goods:
#     print(key, ") ", goods[key][0], " - ", goods[key][1], " шт. по ", goods[key][2], " руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Кол-во: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение некорректное. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
# for key in goods:
#     print(key, ") ", goods[key][0], " - ", goods[key][1], " шт. по ", goods[key][2], " руб.", sep="")

# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d)
# del d['x1']
# d['x4'] = 10
# print(d)
# print(d.values())
# print(d.keys())
# print(d.items())
# # for key, value in d.items():
# #     print(key, "->", value)
# print(list(d))  # ['x1', 'x2', 'x3']
# print(list(d.values()))  # [3, 7, 5]
# print(list(d.items()))  # [('x1', 3), ('x2', 7), ('x3', 5)]


# d = {'x1': 3, 'x2': 7, 'x3': 5}
#
# d2 = d.copy()
# print("d =", d)
# print("d2 =", d2)
#
# d2["x4"] = 10
# d['x1'] = 100
#
# print("d =", d)
# print("d2 =", d2)

# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d["x1"])
# value = d.get("x2", "Такого ключа не существует")  # получает значение ключа, при отсутствии ключа не дает исключение
# print(value)
# item = d.pop("x2", 0)
# print(item)
# print(d)
# item2 = d.popitem()
# print(item2)
# print(d)
# d.clear()
# print(d)


# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d)
# item = d.setdefault("x1", 10)
# print(item)
# print(d)
# a = {"one": 1, "two": 2, 'x1': 10}
# print(a)
# a = tuple(a.items())
# print(a)
# d.update(a)
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y
# # z = x.copy()
# # z.update(y)
# print(z)

# d = dict.fromkeys(['a', 'b'], 100)
# print(d)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d2 = dict()
# d2['name'] = d.pop('name')
# d2['salary'] = d.pop('salary')
# print(d)
# print(d2)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)

# d = {
#     'first': {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     'second': {
#         4: "four",
#         5: "five"
#     }
# }
# print(d)
#
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ":", d[x][y])

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# d2 = {key: value for key, value in d.items() if value <= 2}
# print(d2)


# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
# for i in lst:
#     if type(i) == str:
#         d[i] = []  # d['one'] = []
#         s = i  # s = 'one'
#     else:
#         d[s].append(i)  # d['one'].append(1 | 2 | 3)
#
# print(d)


# zip()

# one = [1, 2, 3, 4, 5]
# two = ["one", "two", "three"]
# three = [2.5, 4.6, 8.9]

# d = dict(zip(one, two))
# print(d)

# # lst = list(zip(one, two, three))
# lst = list(zip(one))
# print(lst)

# f = {k: v for k, v in zip(one, two)}
# print(f)

# one = {"name": "Igor", "surname": "Doe", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Smith", "job": "Manager"}
# three = {"name": "Irina", "surname": "Smith", "job": "Manager"}

# for (k1, v1), (k2, v2), (k3, v3) in zip(one.items(), two.items(), three.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)
#     print(k3, "->", v3)

# lst = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*lst)
# print(a)  # (1, 2, 3)
# print(b)  # ('one', 'two', 'three')

# a = {"one": 1, "two": 2, "three": 5}
# b = {"three": 3, "four": 4}
# print({**a, **b})  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# for k, v in {**a, **b}.items():
#     print(k, "->", v)

# data = [5, 7, 9, 4, 1, 3, 5, 8, 6, 4]
# j = 1 
# for i in data:
#     print(j, ") ", i, sep="")
#     j += 1

# data = [5, 7, 9, 4, 1, 3, 5, 8, 6, 4]

# for j, i in enumerate(data, 1):
#     print(j, ") ", i, sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args


# print(func(5))
# print(func(5, 6, 7, "abc"))
# print(func())


# def summa(*param):
#     res = 0 
#     for i in param:
#         res += i 
#     return res


# print(summa(1, 8, 9, 6, 5, 4, 7, 3, 5, 1, 4, 2, 6))
# print(summa(5, 4, 7, 3, 5, 1, 4))
# print(summa(4, 2, 6))

# def to_dict(*args):
#     d = {}
#     for i in args:
#         d.update({i: i})
#     return d
#     # return dict(zip(args, args))


# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))

# def ch(*args):
#     average = sum(args) / len(args)
#     print(average)
#     res = []
#     for num in args:
#         if average > num:
#             res.append(num)
#     return res


# print(ch(1,2,3,4,5,6,7,8,9))
# print(ch(3,6,1,9,5))

# def func(a, *args):
#     return a, args


# print(func(5))
# print(func(5,9,8,7,6))

# def print_scores(student, *scores):
#     print("Name:", student)
#     for score in scores:
#         print(score, end=" ")
#     print()


# print_scores("Roman", 5,4,3,5,4,5,5,3,5)
# print_scores("Nikita", 5,5,3,5)

# def func(**kwargs):
#     return kwargs


# print(func(a=1, b=2, c=3))
# print(func())
# print(func(name="Python"))

# def intro(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "is", v)
#     print()


# intro(name="Irina", surname="Sharma", age=22)
# intro(name="Igor", surname="Wood", email="igor@gmail.com", age=22, phone=987654321)

# def func(a, b, *args, dd=5, **kwargs):
#     return a, b, args, kwargs, dd


# print(func(1,2,3,4,5, aa=1, bb=2, cc=3))

# def db(**kwargs):
#     my_dict.update(**kwargs)


# my_dict = {"one": "first"}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name="Bob", age=31, weight=61, eyes_color="grey")
# print(my_dict)

# name = "Tom"  # глобальная переменная
# surname = ""


# def hi():
#     global name, surname
#     name = "Sam"  # локальная переменная
#     surname = "Johnson"
#     print("Hello", name, surname)


# def bye():
#     print("Good bye", name)


# print(name)   
# hi()
# bye()
# print(name)
# print(surname)

# i = 5


# def func(arg=i):
#     print(arg)


# i = 6
# func()  # 5


# x =10 # 3 уровень приоритета


# def func(a):
#     x = 2  # 2 уровень приоритета

#     def inner():
#         x = 6  #  самый высокий приоритет
#         print("x:", x)
#         return a + x  

#     return inner()

# print(func(3))


# sum = "Hello"
#
# print(sum)
#
# lst = [1, 2, 3, 4, 5]
# print(sum(lst))

# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World!")


# def fun1():
#     a = 6  # 2
#
#     def fun2(b):
#         a = 4  # 5
#         print(a + b)  # 6
#
#     print("a:", a)  # 3
#     fun2(4)  # 4
#
#
# fun1()  # 1

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# q = x + t
# print(q)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x  # перезаписывает переменную на уровень выше
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print("a:", a)
#         # print("b:", b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# Замыкание

# def outer(n):  # 5
#     def inner(x):  # 10
#         return n + x
#
#     return inner
#
#
# out1 = outer(5)
# print(out1(10))
#
# out2 = outer(6)
# print(out2(4))


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()
# res2()
# res2()
#
# res1()


# lambda - функция (выражение)


# def func(x, y):
#     return x + y
#
#
# print(func(2, 3))

# print((lambda x, y: x + y)(2, 3))
# print((lambda x, y: x + y)(12, 3))

# variable = (lambda x, y: x + y)
#
# print(variable(2, 3))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())
#
# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6))
# print((lambda *args: args)("a", "b", "c"))


# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t("abc_"))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: n + x
#
#
# outer2 = lambda n: lambda x: n + x
#
# f2 = outer2(5)
# print(f2(10))
#
# print((lambda n: lambda x: n + x)(5)(10))

# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# d = {"b": 15, "a": 7, "c": 3}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))


# players = [
#     {'name': 'Антон', 'last_name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last_name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last_name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last_name': 'Семенов', 'rating': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item['last_name'])
# print(res1)
# res2 = sorted(players, key=lambda item: item['rating'])
# print(res2)
# res3 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res3)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y]
# b = a[2](5, 3)
# print(b)


# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
# }
#
# d[3]()


# print((lambda a, b: a if a > b else b)(5, 13))
# print((lambda a, b, c: a if (a < b) and (a < c) else b if (b < c) and (b < a) else c)(12, 5, 6))
# print((lambda *args: min(args))(12, 5, 6))
# print((lambda *args: sorted(args)[0])(12, 5, 6))


# map(func, iterable), filter(func, iterable)


# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# lt = list(map(mult, lst))
# print(lt)
#
# lt1 = list(map(lambda t: t * 2, lst))
# print(lt1)
#
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))

# lst = ['1', '2', '3', '4', '5']
# print(lst)
# print(list(map(lambda x: int(x), lst)))
# print(list(map(int, lst)))
# print([int(i) for i in lst])

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda x, y: {x, y}, st, num)))

# st = [9, 2, 7, 6, 5]
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: x + y, st, num)))

# t = ('abcd', 'abc', 'cdefg', 'def', 'gth')

# t2 = tuple(filter(lambda s: len(s) == 3, t))
# t2 = list(filter(lambda s: s, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, b)))

# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# print(list(filter(lambda a: 10 <= a <= 20, lst)))

# Вывести квадраты нечетных чисел от 1 до 10
# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))
# print([x ** 2 for x in range(1, 10) if x % 2])


# Декораторы


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(id(test))
# print(id(hello))
# print(test())

# def my_decorator(func):
#     def inner():
#         print('Code before')
#         func()
#         print('Code after')
#     return inner
#
#
# def func_test():
#     print('Hello')
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):
#     def inner():
#         print('*' * 50)
#         func()
#         print('-' * 50)
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello')
#
#
# func_test()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
# #
# #
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
# #
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
# #
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
# #
# #
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
# #
# #
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Мумладзе")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
# #
# #
# @args_decorator
# def func(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
# #
# # @args_decorator
# def func1(study):
#     print("Мне нравится", study)
# #
# #
# func("Борис", "Елизавета", "Светлана", study="JavaScript")
# func("Владимир", "Екатерина", "Виктор")
# func1(study="HTML")

# def decor_args(arg1, arg2):
#     def decor(fn):
#         def wrap(x, y):
#             print(arg1, x, arg2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return decor
# #
# #
# @decor_args("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
# #
# #
# @decor_args("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
# #
# summa(5, 2)
# sub(5, 2)


# def multiply(arg1):
#     def decor(fn):
#         def wrap(x):
#             return arg1 * fn(x)  # 3 * 5
#
#         return wrap
#
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# Строки

# print(int("19"))
# print(int("19.5"))
# print(int(19.5))

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))


# print(bin(18))  # 0b10010 - двоичная
# print(oct(18))  # 0o22 - восьмеричная
# print(hex(18))  # 0x12 - шестнадцатеричная
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0b10010 + 0x12)


# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 2)
# print("y1" in e)
# print(e[0])
# print(e[1:3])

# s = "Python"  # Pytton
# # s[3] = "t"
# s = s[:3] + 't' + s[4:]
# print(s)

# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == old:
#             s2 = s2 + new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = change_char_to_str(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)

# print("Привет")
# print(u"Привет")

# print("C:\\folder\\fil\nes.txt\\")
# print(r"C:\folder\files\\"[:-1])
# print(r"C:\folder\files" + "\\")

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# ch = 5.26987412
#
# print(f"Число: {round(ch, 3)}")
# print(f"Число: {ch:.3f}")

# x = 10
# y = 5
# print(f"{x = }, {y = }")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# num = 74
#
# print(f"{{{{{num}}}}}")
#
# print("C:\\\\text")

# dir_name = 'my_doc'
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)

# s = '''
# Несколько
# строк
# '''
# print(s)
#
# s1 = """
# Несколько
# строк
# """
# print(s1)
#
# s2 = "Несколько строк"
# print(s2)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n."""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)
# print(max.__doc__)
# print(list.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('й'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# s = "Test string for met"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [sum(arr) // len(arr)] + arr  # ср. арифм. впереди списка
# print(arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(f"Количество последних элементов: {arr.count(arr[-1]) - 1}")
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(8364))

# a = 97
# b = 122
#
# if a < b:
#     a, b = b, a
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# print("apple" == "Apple")
# print("apple" > "Apple")  # 97 > 65


# from random import randint
#
# shortest = 7
# longest = 10
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):  # range(10)
#         rand_char = chr(randint(min_ascii, max_ascii))
#         res += rand_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())


# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.

# print(s.count("l"))
# print(s.count("l", 3))
# print(s.count("l", 3, 10))

# print(s.find("Python"))  # возвращает первое вхождение подстроки в строку, если такой нет - возвращает -1
# print(s.find("l", 4, 20))
# print(s.find("l"))
# print(s.rfind("l"))
#
# print(s.index("l"))  # ValueError
# print(s.rindex("l"))


# st = input("Введите два слова через пробел: ")
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
# print(f"{second} {first}")
# print(s.startswith("I am", 14))
# print(s.index("I am"))
# print(s.endswith("on."))


# print('123'.isdigit())  # только числа
# print('qqwewe'.isalpha())  # только буквы
#
# print('Abc123'.isalnum())  # только буквы или цифры
#
# print('abc'.islower())  # только буквы в нижнем регистре и другие символы
# print('ФBC01123'.isupper())  # только буквы в верхнем регистре и другие символы

# n = input("Введите число: ")
# if n.isdigit():
#     n = int(n)
#     print(n * 2)


# print('py'.center(10))
# print(' py '.center(11, "-"))


# print('   py   '.lstrip())
# print('   py   '.rstrip())
# print('   py   '.strip())

# print('https://www.pythons.org'.strip('/:pths.org'))
# print('https://www.pythons.org'.lstrip('/:pths').rstrip('.org'))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("N", "P"))
# print(str1.replace("Nython", "Python"))

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '99']))
#
# print(":".join("Hello"))

# print("Строка разделенная пробелами".split())  # ['Строка', 'разделенная', 'пробелами']
# print('www.python.org.ru'.split(".", 2))
# print('www.python.org.ru'.rsplit(".", 2))

# a = input("-> ").split()
# b = list(map(int, a))
# print(b)


# Регулярные выражения


# import re

# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта."
# reg = "я"

# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта. 98673"
# reg = "[0-9][0-9][0-9][0-9]"
#
# print(re.findall(reg, s))  # возвращает список содержащий все совпадения
#
# print(re.search(reg, s))  # месторасположение первого совпадения с объектом
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# print(re.match(reg, s))  # поиск совпадения с шаблоном вначале строки
#
# print(re.split(reg, s))  # возвращает список, в котором строка разбита по шаблону
#
# print(re.sub(reg, "!", s))  # поиск и замена

# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 198673 Hello"
# reg = "[21][0-9][0-9][0-9]"
# reg = "[А-яЁё]"
# reg = "[A-Za-z]"
# reg = r"\."
# reg = r"[A-Za-z\[\]-]"
# reg = r"[^0-9]"
# reg = r"[^А-яЁёA-Za-z0-9]"
# print(re.findall(reg, s))

# print(ord('Я'))
# print(ord('а'))


# st = "Час в 24 формате от 00 до 23. 2021-06-15Т19:50. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09."
# pattern = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(pattern, st))


# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 198673 Hel_lo"
# reg = r"20*"
# print(re.findall(reg, s))

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# reg = r'[+-]?[\d.]+'
# print(re.findall(reg, d))


# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"\s#.*", "", s))
# print(re.sub('-', '.', s))
# print("Дата рождения:", re.sub('-', '.', re.sub(r"\s#.*", "", s)))

# s = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# reg = r'\w+\s*=\s*[^;]+'
# print(re.findall(reg, s))

# s = "12 сентября 2024 года 568789456"
# reg = r"\d{2,4}"
# print(re.findall(reg, s))

#
# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё_та."
# # reg = r"^\w+\s\w+"
# reg = r"\w+\.$"
# print(re.findall(reg, s))

# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9-]{3,16}$", login)
#
#
# print(validate_login("Python-master"))

# import re

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "Hello world"
# print(re.findall(r"\w\+", text, re.DEBUG))

# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта."
# reg = "я"
#
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.findall(reg, s, re.I))

# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall('''
# [A-Za-z0-9._-] +  # part 1
# @                 # @
# [A-Za-z.-]+       # part 2
# ''', 'test@mail.ru', re.VERBOSE))

# text = """Python
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

# s = "Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0"
# reg = r"\w+\s*=\s*\d[.\w]*"
# reg = r"int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*"
# reg = r"(?:int|float)\s*=\s*\d[.\w]*"  # (?: ...) - группирующая скобка не является сохраняющей
# reg = r"(int|float)\s*=\s*\d[.\w]*"
# print(re.findall(reg, s))
# print(re.search(reg, s))

# s = "5 + 7*2 - 4"
# reg = r"(\s*[+*-]\s*)"
# print(re.split(reg, s))

# s = "01-12-2024"
# reg = "(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])
# print(m[3])
# print(re.search(reg, s).group(0))
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))
# print(re.search(reg, s).group(3))

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", replace_find, text))

# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024."  # 23.10.2024 24.10.2024
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"([a-z0-9-]{2,}\.[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))


# Рекурсия

# def elevator(n):  # 5
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)  # 5
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):  # [1, 3, 5, 7, 9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + ...
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def to_str(n, base):  # 15, 16
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # convert[15] = 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] = 'E'
#
#
# print(to_str(254, 16))  # FE

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def remove(text):  # ""
#     if not text:  # text = ""
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])  # ""
#     else:
#         return text[0] + remove(text[1:])  # "HelloWorld" + ""
#
#
# print(remove("  Hello\nWorld "))


# Файлы


# f = open("test.txt", "r")
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# print(f.closed)

# f = open("test.txt", "r")
# f = open(r"C:\Users\user\OneDrive\Документы\Курс Python317\Python317\test.txt", "r")
# print(f.read(3))  # возвращает весь документ
# print(f.read())
# f.close()
#
# f = open("test2.txt", "r")
# print(f.readline())  # возвращает одну строку
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open("test2.txt", "r")
# print(f.readlines(26))  # возвращает список строк
# print(f.readlines())
# f.close()

# f = open("test2.txt", "r")
# print(len(f.readlines()))
# f.close()

# f = open("test2.txt", "r")
# count = 0
# for line in f:
#     print(line, end="")
#     count += 1
# f.close()
# print(count)

# f = open("xyz.txt", 'w')
# f.write("Hello\nWorld!\n")
# f.close()


# f = open("xyz.txt", 'a')
# f.write("New text.\n")
# f.close()

# f = open("xyz.txt", 'a')
# lines = ['\nThis is line 1', '\nThis is line 2']
# f.writelines(lines)
# f.close()

# f = open("xyz.txt", 'w')
# lst = [str(i) + " " for i in range(1, 20)]
# print(lst)
# # for index in lst:
# #     f.write(index + "\t")
# f.writelines(lst + " ")
# f.close()


# f = open("test3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл\n")
# f.close()

# f = open('test3.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello world\n"
# print(read_file)
# f.close

# f = open("test3.txt", "w")
# f.writelines(read_file)
# f.close()

# f = open("test3.txt", "r")
# read_file = f.readlines()
# pos = int(input("Введите индекс строки для удаления: "))
# if 0 <= pos < len(read_file):
#     del_pos = read_file.pop(pos)
# else:
#     print("Индекс введен неверно")
# f.close()
#
# f = open("test3.txt", 'w')
# f.writelines(read_file)
# f.close()

# f = open("test.txt", "r")
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию условного курсора в файле
# print(f.seek(1))  # перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("test.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# f = open("test2.txt", "a+")
# # print(f.write("1111 I am learning Python 1111"))
# print(f.read())
# f.close()

# with open("test2.txt", "w+") as f:
#     print(f.write('0123456789'))
# print(f.closed)

# with open("test2.txt", "r") as f:
#     for line in f:
#         print(line[:3])


# file_name = "res.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = map(str, lt)
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     # f.write(str(lst))
#     f.write(get_line(lst))
#
#
# with open(file_name, 'r') as f:
#     st = f.read()
#
# print(st)
#
# nums = list(map(float, st.split()))
# print(nums)
# print(type(nums[0]))

# a = 5

# if a == 5:
#     b = 10

# for i  in range(12):
#     b = 10

# def func():
#     b = 10
#
#
# func()
# print(b)

# def longest_words(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         print(max_length)
#         res = [i for i in w if len(i) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words('test.txt'))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\
# nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)


# with open('one.txt', 'r') as fr, open('two.txt', 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)


# Модуль OS, OS.PATH

# import os
# import time


# import os.path


# print(os.getcwd())  # возвращает текущую директорию
# print(os.listdir())  # список директорий и файлов
# print(os.listdir(".."))

# os.mkdir("folder1")  # создает папку
# os.makedirs("nested1/nested2/nested3")  # создает конечную директорию вместе с промежуточными

# os.rmdir("folder1")  # удаление пустой папки
# os.rmdir("nested1/nested2/nested3")

# os.remove("xyz1.txt")  # удаление файла

# os.rename("xyz.txt", "new.txt")  # переименование файла и папки
# os.rename("folder", "new")

# os.rename("two.txt", "nested1/two.txt")
# os.renames("test.txt", "nested1/nested3/two.txt")  # переименование файла и папки, перемещает документы,
# создавая промежуточные директории


# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\t\tFiles:", files)


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена")
#     print('-' * 50)
#
#
# remove_empty_dirs("nested1")

# print(os.path.split(r"C:\Users\user\OneDrive\Документы\Курс Python317\
# Python317\nested1\nested2\nested4\test2.txt"))  # [1] - test2.txt
#
# print(os.path.join(r'C:\Users\user\OneDrive\Документы\
# Курс Python317', 'Python317', 'nested1', 'nested2', 'test2.txt'))

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, 'w').close()
#
# file_with_text = [r'Work\w.txt', r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Текст в файле {file}")

# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

# root = 'files'
# objs = os.listdir(root)
# print(objs)
# objs = list(map(lambda i: os.path.join(root, i), objs))
# print(objs)
#
# obj_sort = sorted(objs, key=os.path.isfile, reverse=True)
# print(obj_sort)

# print(sorted(objs, reverse=True))

# print(os.path.isfile(r"files\one.txt"))  # возвращает True, если путь является файлом
# print(os.path.isdir(r"files\dir"))  # возвращает True, если путь является директорией


# print(os.path.exists(r'nested1\nested2'))  # проверка на существование пути
# print(os.path.getsize(r'nested1\nested2'))  # размер документа в байтах
#
# root = r'nested1\nested2'
# if os.path.exists(root):
#     print(os.path.getsize(root))
#
# b = os.path.getsize(r'main.py')
# print(b, "байт")
# print(b // 1024, "килобайт")

# path = "main.py"
# print(os.path.getctime(path))  # возвращает время создания файла
# print(os.path.getatime(path))  # возвращает время последнего доступа к файлу
# print(os.path.getmtime(path))  # возвращает время последнего изменения файла (в секундах)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getatime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getmtime(path))))


# ООП


# class Point:
#     """Класс для предоставления координат на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(p1.x)
# print(type(p1))
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))


# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 10
# p1.y = 20
# p1.z = 30
# print(p1.x, p1.y, p1.z)
# print(p1.__dict__)
#
# p2 = Point()
# p2.x = 100
# # p2.y = 200
# print(p2.x, p2.y)
# print(p2.__dict__)

# print(id(Point))
# print(id(p1))
# print(id(p2))


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# # Point.set_coord(p1)
#
# p2 = Point()
# # p2.x = 50
# # p2.y = 100
# p2.set_coord(50, 100)
# # Point.set_coord(p2)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, '*'))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: "
#               f"{self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Юлия")
# print(h1.get_name())
# h1.set_birthday("23.12.1990")
# print(h1.get_birthday())
# h1.print_info()

# class Person:
#     skill = 10  # статическое свойство
#     count = 0
#
#     def __init__(self, name, surname):  # инициализатор
#         self.name = name  # динамическое свойство
#         self.surname = surname
#         print("Инициализатор")
#         Person.count += 1
#
#     def __del__(self):  # финализатор (деструктор)
#         print("Удаление экземпляра:", self.__class__.__name__)
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
# # del p1
# # p1 = 5
#
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)
#
# p3 = Person("Анна", "Долгих")
# print(p1.count)
# print(p2.count)
# print(Person.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
# droid3 = Robot('P-2CO')
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим")
# del droid1
# del droid2
# del droid3
# print("Численность роботов:", Robot.k)


# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(a):
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должна быть числом")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата Y должна быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# # p1.set_coord(100.5, 200.3)
# # print(p1.get_coord())
# p1.set_x(50)
# print(p1.get_x())
# p1.set_y(30)
# print(p1.get_y())
# p1._Point__x = 111
# print(p1.__dict__)
# print(p1._Point__x)

# from math import sqrt


# class Rectangle:
#     __slots__ = ["__length", "__width", "x"]
#
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(a):
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimeter(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return round(sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# rect = Rectangle(4, 12)
# rect.set_length(3)
# rect.set_width(9)
# print("Длина прямоугольника", rect.get_length())
# print("Ширина прямоугольника:", rect.get_width())
# print("Площадь прямоугольника:", rect.get_area())
# print("Периметр прямоугольника", rect.get_perimeter())
# print("Гипотенуза прямоугольника", rect.get_hypotenuse())
# rect.get_draw()
# rect.x = 20
# print(rect.x)
# print(rect.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         self.__x = x
#         print("Сеттер")
#
#     def __get_x(self):
#         print("Геттер")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(a):
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.deleter
#     def x(self):
#         del self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100.2
# print(p1.x)
# # del p1.x
# print(p1.__dict__)


#  Создать класс для преобразования килограмм в фунты
# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", weight.to_pound(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг =>", weight.to_pound(), "фунтов")
# weight.kg = "два"


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# p4 = Point()
# p5 = Point()
#
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# ch = Change()
# print(ch.inc(10), Change.dec(10))

# class Fact:
#     @staticmethod
#     def max(*args):
#         return max(args)
#
#     @staticmethod
#     def min(*args):
#         return min(args)
#
#     @staticmethod
#     def fact(arg):
#         factor = 1
#         for i in range(1, arg + 1):
#             factor *= i
#         return factor
#
#     @staticmethod
#     def avg(*args):
#         return sum(args) / len(args)
#
#
# print(Fact.max(3, 5, 7, 9))
# print(Fact.min(3, 5, 7, 9))
# print(Fact.fact(5))
# print(Fact.avg(3, 5, 7, 9))


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     "15.12.2024",
#     "23-10-2023",
#     "01.01.2021",
#     "12.31.2020"
# ]
#
# for d in dates:
#     if Date.is_date_valid(d):
#         date = Date.from_string(d)
#         print(date.string_to_db())
#     else:
#         print("Неправильная дата или формат строки с датой")

# date2 = Date.from_string("23.10.2023")
# print(date2.string_to_db())
# date3 = Date.from_string("15.12.2024")
# print(date3.string_to_db())

# day, month, year = map(int, string_date.split("."))
# date = Date(day, month, year)
# print(date.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         usd_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {usd_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()


# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall('[a-zа-яё-]', fio, re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом от 14 до 120")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 30:
#             raise TypeError("Вес должен быть вещественным числом от 30 и больше ")
#
#     @staticmethod
#     def verify_password(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, value):
#         self.verify_weight(value)
#         self.__weight = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         self.verify_password(value)
#         self.__password = value
#
#
# p1 = UserDate("Волков2 Игорь Николаевич", 24, "1234 567890", 80.8)
#
# # p1.fio = "Соболев Игорь Николаевич"
# print(p1.__dict__)


# class Point:  # (object)
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# # print(issubclass(Point, object))
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print("Переопределенный инициализатор Prop")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         print("Переопределенный инициализатор Line")
#
#     def draw_line(self):  # -> None
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def draw_rect(self):  # -> None
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# # print(line._color)
#
# line.draw_line()
# # rect = Rect(Point(30, 40), Point(70, 80))
# # rect.draw_rect()
# # print(issubclass(Line, Prop))
# # print(issubclass(Line, Rect))
# # print(Point.__dict__)
# # print(Line.__dict__)
# # print(Prop.__dict__)


# class Figure:
#     def __init__(self, color):
#         self.color = color
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть положительным числом")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.color)
# # rect.width = 50
# # print(rect.width)
# print(rect.area())

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник: \nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self,width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, px, solid, red):
#         super().__init__(width, height)
#         self.px = px
#         self.solid = solid
#         self.red = red
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Рамка: {self.px} {self.solid} {self.red}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px", "solid", "red")
# shape2.show_rect()

# class Vector(set):
#     def __str__(self):
#         # return " ".join(map(str, self))
#         return " ".join(self)
#
#
# # v = Vector({1, 2, 3})
# v = Vector({"b", "a", "c"})
# print(v)


# class Point:  # (object)
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def draw_line(self):  # -> None
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp: Point = None, ep: Point = None):
#         if ep is None:
#             self._sp = sp
#         elif sp is None:
#             self._ep = ep
#         else:
#             self._sp = sp
#             self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(12, 18), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20))
# line.draw_line()
# #
# line.set_coord(ep=Point(500, 700))
# line.draw_line()


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть реализован метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     ...
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(30, 30)))
#
# for f in figs:
#     f.draw()


# Абстрактные методы
# Абстрактный класс

# from abc import ABC, abstractmethod


# class Chess(ABC):  # Абстрактный класс - работает с абстрактным методом
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):  # абстрактный метод - используется только с абстрактным классом
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на е2е4")
#
#
# q = Queen()
# q.draw()
# q.move()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = SqTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def show(self):
#         print(f"= {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#     def show(self):
#         print(f"= {self.convert_to_rub():.2f} RUB")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#     def show(self):
#         print(f"= {self.convert_to_rub():.2f} RUB")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     elem.show()
#
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for elem in e:
#     elem.print_value()
#     elem.show()


# Интерфейсы

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#
#
# ch = GrandChild()
# ch.display1()
# ch.display2()


# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         print("outer_method")
#
#     def instance_method(self):
#         print("instance_method")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Вложенный метод", MyOuter.age, self.obj.name)
#             MyOuter.outer_method()
#             self.obj.instance_method()
#
#
# out = MyOuter('внешний')
# print(out.name)
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()

# class DarkGreen:
#     def __init__(self):
#         self.name = "Dark Green"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#         self.dg = DarkGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# g2 = outer.dg
# g2.display()
# print(g2.name)

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = Computer().OS()
# my_cpu = Computer().CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = [Cat("Пушок")]
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.coord = args  # tuple()
#         self.color = "red"
#         self.width = 2
#
#     def __len__(self):
#         return len(self.coord)
#
#
# p = Point(1, 2, 5)
# print(len(p))
#
# s = list((1, 2))
# print(len(s))

# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(10, 20)
# print(p1.x, p1.y)
# # p1.z = 30
# # print(p1.z)
# p1.length = 20
# print(p1.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2(1, 2)
# print("pt1 =", pt1.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt1 = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 3
# print(pt3.z)


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.sleep()
# beast.play()


# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса АA")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#         B.__init__(self)
#         C.__init__(self)
#
#
# d = D()
# print(D.mro())
# # print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         # Styles.__init__(self, color, width)
#         super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self. _width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()
#
# print(Line.mro())


# Миксины

# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init Mixin")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
#
# n1 = NoteBook("HP", 1.5, 35000)
# n1.print_info()
# n1.save_sell_log()


# Перегрузка операторов

# 24 * 60 * 60 = 86400 - число секунд в одном дне

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec == other.sec:
#             return True
#         return False
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec < other.sec:
#             raise AttributeError("Правый операнд должен быть меньше или равен левому")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec < other.sec:
#             raise AttributeError("Правый операнд должен быть меньше или равен левому")
#         if other.sec == 0:
#             raise ZeroDivisionError("Правый операнд не может быть нулем")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec < other.sec:
#             raise AttributeError("Правый операнд должен быть меньше или равен левому")
#         if other.sec == 0:
#             raise ZeroDivisionError("Правый операнд не может быть нулем")
#         return Clock(self.sec % other.sec)
#
#     def __gt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec > other.sec:
#             return True
#         return False
#
#     def __lt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec < other.sec:
#             return True
#         return False
#
#     def __ge__(self, other):
#         return not self.__lt__(other)
#
#     def __le__(self, other):
#         return not self.__gt__(other)

#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "min":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 11
# c1["min"] = 24
# c1["sec"] = 59
# print(c1["hour"], c1["min"], c1["sec"])

# c1 = Clock(400)
# c2 = Clock(300)
# # c4 = Clock(300)
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c4.get_format_time())
# c3 = c1 + c2 + с4
# print(c3.get_format_time())
# c1 += c2
# print(c1.get_format_time())
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время равно")

# c3 = c1 - c2
# print(c3.get_format_time())
# c1 -= c2
# print(c1.get_format_time())
# c3 = c1 * c2
# print(c3.get_format_time())
# c1 *= c2
# print(c1.get_format_time())
# c3 = c1 // c2
# print(c3.get_format_time())
# c1 //= c2
# print(c1.get_format_time())
# c3 = c1 % c2
# print(c3.get_format_time())
# c1 %= c2
# print(c1.get_format_time())

# print(c1 > c2)
# print(c1 >= c2)
# print(c1 < c2)
# print(c1 <= c2)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):  # 10 >= 5
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)  # [5, 5, 3, 4, 5, None, None, None, None, None, None]
#         self.marks[key] = value  # [5, 5, 3, 4, 5, None, None, None, None, None, 4]
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)

# print([None] * 6)
# lst = [5, 5, 3, 4, 5]
# lst.extend([None, None, None, None, None, None])
# print(lst)


# написать программу разведения котов и кошек с предполагаемым количеством котят

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)


# Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())

# from abc import abstractmethod, ABC
#
#
# class Animal(ABC):
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     @abstractmethod
#     def info(self):
#         pass
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Cat(Animal):
#     def info(self):
#         return f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} мяукает"
#
#
# class Dog(Animal):
#     def info(self):
#         return f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} гавкает"
#
#
# cat1 = Cat("Пушок", 2.5)
# dog1 = Dog("Мухтар", 4)
#
# for animal in (cat1, dog1):
#     print(animal.info())
#     print(animal.make_sound())
#
# print(dog1.info())
# print(dog1.make_sound())


# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.last_name} {self.first_name} {self.age}", end=" ")
#
#
# class Student(Human):
#     def __init__(self, last_name, first_name, age, speciality, group, rating):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, last_name, first_name, age, speciality, experience):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.experience}", end=" ")
#
#
# class Graduate(Student):
#     def __init__(self, last_name, first_name, age, speciality, group, rating, topic):
#         super().__init__(last_name, first_name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end=" ")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()


# Функторы


# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1(" :?.Hello World! "))  # Hello World
#
#
# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(self.__chars)
#
#     # def __call__(self, *args, **kwargs):
#     #     if not isinstance(args[0], str):
#     #         raise ValueError("Аргумент должен быть строкой")
#     #
#     #     return args[0].strip(self.__chars)
#
#
# s2 = StripChars("?:!.; ")
# print(s2(" :?.Hello World! "))

# Класс как декоратор

# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self):
#         print('Перед вызовом функции')
#         self.fn()
#         print('После вызова функции')
#
#
# @MyDecorator
# def func():
#     print("Hello World")
#
#
# func()


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         # print('Перед вызовом функции')
#         # res = self.fn(x, y)
#         # print('После вызова функции')
#         # return res
#         return f"Перед вызовом функции\n{self.fn(x, y)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class Power:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         return f"Результат: {self.func(x, y) ** 2}"
#
#
# @Power
# def func_test(a, b):
#     return a * b
#
#
# print(func_test(2, 3))


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         return f"Перед вызовом функции\n{self.fn(*args, **kwargs)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func1(2, 5, 2))
# print(func1(2, c=5, b=2))


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             return f"Перед вызовом функции\n{self.arg} {args[0]} x {args[1]} = {fn(*args, **kwargs)}\nПосле вызова " \
#                    f"функции"
#
#         return wrap
#
#
# @MyDecorator("Произведение:")
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class Power:
#
#     def __init__(self, power):
#         self.power = power
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             # print("args:", args)
#             # print("kwargs:", kwargs)
#             return f"Результат: {func(*args, **kwargs) ** self.power}\n"
#         return wrapper
#
#
# @Power(3)
# def func_test(a, b):
#     return a / b
#
#
# print(func_test(4, 2))
# print(func_test(b=4, a=2))

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Некрасов")
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(5))
# print(obj.doubler(5))


# Дескриптор

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def get(self):
#         return self.__value
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__value = value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__surname = value
#
#
# p = Person("Иван", "Петров")
# print(p.name.get())
# p.name.set("Игорь")
# print(p.name.get())

# Дескриптор (__get__, __set__, __set_name__, __delete__)

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Иван", "Петров")
# p.surname = "Иванов"
# print(p.name)
# print(p.surname)

# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f"Значение {self.name} должно быть положительным")
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple_order = Order('apple', 5, 10)
# apple_order.quantity = 15
# print(apple_order.price)
# print(apple_order.total())
# print(apple_order.__dict__)


# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# print(lst, lst.get_length())  # [5, 7] 2

# Создание модулей

# import geometry.rect
# import geometry.sq
# import geometry.trian

# from geometry import *
# from geometry import rect, sq, trian
#
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()


# from car import elecrtrocar
# from car.elecrtrocar import ElectroCar
#
# # e_car = elecrtrocar.ElectroCar("Tesla", "T", 2018, 99000)
# e_car = ElectroCar("Tesla", "T", 2018, 99000)
# e_car.show_car()
# e_car.description_battery()


# class Employee:
#     def __init__(self, kod, name):
#         self.id = kod
#         self.name = name
#
#
# class SalaryEmployee(Employee):
#     """Административные работники, имеют фиксированную зарплату"""
#
#     def __init__(self, kod, name, weekly_salary):
#         super().__init__(kod, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
#
# class HourlyEmployee(Employee):
#     """Сотрудники с почасовой оплатой"""
#
#     def __init__(self, kod, name, hours_worked, house_rate):
#         super().__init__(kod, name)
#         self.hours_worked = hours_worked
#         self.house_rate = house_rate
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.house_rate
#
#
# class CommissionEmployee(SalaryEmployee):
#     """Торговые представители, фиксированная зарплата + комиссия"""
#
#     def __init__(self, kod, name, weekly_salary, commission):
#         super().__init__(kod, name, weekly_salary)
#         self.commission = commission
#
#     def calculate_payroll(self):
#         fixed = super().calculate_payroll()
#         return fixed + self.commission
#
#
# class PayrollSystem:
#     def calculate(self, employees):
#         print("Расчет заработной платы")
#         print("=" * 50)
#         for employee in employees:
#             print(f"Заработная плата: {employee.id} - {employee.name}")
#             print(f"- Проверить сумму: {employee.calculate_payroll()}")
#             print()
#
#
# salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
# hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
# commission_employee = CommissionEmployee(3, "Николай Хорольский", 1000, 250)
# payroll_system = PayrollSystem()
# payroll_system.calculate([
#     salary_employee,
#     hourly_employee,
#     commission_employee
# ])


# Упаковка данных
# сериализация
# десериализация

# marshal (*.рус)
# pickle:
# dump() - сохраняет данные в открытый файл
# load() - получает данные из файла
# dumps() - сохраняет данные в строку
# loads() - получает данные из строки
# json

# import pickle

# file_name = "basket.txt"
#
# shop_list = {
#     "фрукты": ("яблоки", "манго"),
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
#
# with open(file_name, "rb") as f:
#     shop_list2 = pickle.load(f)
#
# print(shop_list2)


# class Text:
#     num = 35
#     string = "Привет"
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#
#     def __str__(self):
#         return f"Число: {Text.num}\nСтрока: {Text.string}\nСписок: {Text.lst}\nКортеж: {Text.tpl}"
#
#
# obj = Text()
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# obj2 = pickle.loads(my_obj)
# print(obj2)

#
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# import json

# data = {
#     'name': 'Ольга',
#     'age': 20,
#     20: None,
#     True: 1,
#     'hobbies': ('running', 'singing'),
#     'children': ['Alica', 'Bob']
# }

# with open('data_file.json', 'w') as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)
#
# with open("data_file.json", 'r') as f:
#     data1 = json.load(f)
# #
# print(data1)
#
# json_string = json.dumps(data, ensure_ascii=False)
# print(json_string)
# print(type(json_string))
# data1 = json.loads(json_string)
# print(data1)
# print(type(data1))


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))  # [{}, {}, {}, {}, {}]
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)  # [{}, {}, {}, {}, {}, {}, {}]
#     with open("persons.json", "w") as f:
#         json.dump(data, f, indent=2)  # [{}, {}, {}, {}, {}, {}, {}]
#
#
# for i in range(5):
#     write_json(gen_person())
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # a = ''
#         # for i in self.marks:
#         #     a += str(i) + ", "
#         # return f"Студент: {self.name} => {a[:-2]}"
#         a = ", ".join(map(str, self.marks))
#         return f"Студент: {self.name} => {a}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def get_file_name(self):
#         return self.name.lower() + ".json"
#
#     def dump_to_json(self):
#         data = {"name": self.name, "marks": self.marks}
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = "\n".join(map(str, self.students))
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(gr1, gr2, index):
#         gr2.add_student(gr1.remove_student(index))
#
#     def get_file_name(self):
#         return self.group.lower().replace(" ", "-") + ".json"
#
#     def dump_to_json(self):
#         data = [
#             {'name': student.name, "marks": student.marks} for student in self.students
#         ]
#         with open(self.get_file_name(), 'w') as f:
#             json.dump(data, f, indent=2)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#     def add_db(self):
#             try:
#                 data = json.load(open('db.json'))
#             except FileNotFoundError:
#                 data = {}
#             js = [
#                 {student.name: student.marks} for student in self.students
#             ]
#             data[self.group] = js
#             with open("db.json", "w+") as f:
#                 json.dump(data, f, indent=2)
#             print(f"Группа {self.group} добавлена в файл")
#
#     @staticmethod
#     def load_groups(file):
#         with open(file, "r") as f:
#             print(json.load(f))

#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(2)
# print(st1)
# st1.edit_mark(2, 5)
# print(st1)
# print(st1.average_mark())
# st1.dump_to_json()
# st1.load_from_file()
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st2.dump_to_json()
# st2.load_from_file()
# st2.add_mark(5)
# print(st2)
# st2.dump_to_json()
# st2.load_from_file()
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts1 = [st1, st2]
# group1 = Group(sts1, "ГК Python")
# # print(group1)
# # print()
# group1.add_student(st3)
# # print(group1)
# # print()
# group1.remove_student(1)
# print(group1)
# print()
# sts2 = [st2]
# group2 = Group(sts2, "ГК Web")
# print(group2)
# Group.change_group(group1, group2, 0)
# print()
# print(group1)
# print()
# print(group2)
# group2.dump_to_json()
# group2.load_from_file()
# group1.dump_to_json()
# group1.load_from_file()
# group1.add_db()
# group2.add_db()
#
# file_name = "db.json"
# Group.load_groups(file_name)


# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def load(file_name):
#         # data = None
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#         finally:
#             return data
#
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         data[new_country] = new_capital
#
#         with open(file_name, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def delete_country(file_name):
#         del_country = input("Введите название страны: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(file_name, 'w') as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def search_data(file_name):
#         country = input("Введите название страны: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             print(f"Страна {country.capitalize()} столица {data[country].capitalize()} есть в словаре")
#         else:
#             print(f"Страны {country.capitalize()} нет в словаре")
#
#     @staticmethod
#     def edit_data(file_name):
#         country = input("Введите страну для корректировки: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             new_capital = input("Введите новое значение столицы: ").lower()
#             data[country] = new_capital
#             with open(file_name, 'w') as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print({k.capitalize(): v.capitalize() for k, v in json.load(f).items()})
#
#
# file = "list_capital.json"
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n"
#                   "3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n"
#                   "6 - завершение работы\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введен некорректный номер")


# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# todos_by_user = {}  # {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo['userId']] += 1  # {1: 2}
#         except KeyError:
#             todos_by_user[todo['userId']] = 1  # {1: 1, 2: 1, 3: 1}
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]
#
# max_complete = top_users[0][1]
# print(max_complete)  # 12
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:  # 11 < 12
#         break
#     users.append(str(user))
# print(users)  # ['5', '10']
#
# max_users = " and ".join(users)
# print(max_users)
# print(f"Users {max_users} completed {max_complete} Todos")
#
#
# def keep(todo):
#     completed = todo["completed"]
#     max_count = str(todo["userId"]) in users
#     return completed and max_count
#
#
# with open("filter_file.json", "w") as f:
#     filtered = list(filter(keep, todos))
#     json.dump(filtered, f, indent=2)

# CSV

# import csv

# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1

# with open("data.csv") as f:
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=file_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1


# with open("students.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", 9, 15])
#     writer.writerow(["Саша", 5, 12])
#     writer.writerow(["Маша", 11, 18])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("data_new.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
#
# with open("data_new.csv") as f:
#     print(f.read())


# with open("student1.csv", 'w') as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": 6})
#     file_writer.writerow({"Имя": "Маша", "Возраст": 15})
#     file_writer.writerow({"Имя": "Вова", "Возраст": 14})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# Парсинг

# from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name").text
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# row = soup.find_all("div", {"data-set": "salary"})
# row = soup.find_all("div", {"class": "name"})
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# print(row)

# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
#
# for i in salary:
#     get_salary(i.text)


# import requests

# r = requests.get("https://ru.wordpress.org/")
# print(r.text)
# print(r.status_code)
# print(r.headers)


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[-1]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get('href')
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3").text
#         except AttributeError:
#             name = ""
#
#         try:
#             url = el.find("h3").find("a")['href']
#         except AttributeError:
#             url = ""
#
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#         except AttributeError:
#             snippet = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except AttributeError:
#             active = ""
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except AttributeError:
#             cy = ""
#
#         data = {
#             "name": name,
#             "url": url,
#             "snippet": snippet,
#             "active": active,
#             "cy": cy
#         }
#         write_csv(data)
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a", encoding="utf-8") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def main():
#     for i in range(1, 25):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# from parsers import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# MVC
# Model - модель
# View - вид или представление
# Controller - контроллер


# Сокеты: серверный и клиентский

# import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parser_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found!</h3>'
#     if code == 405:
#         return '<h1>405</h1><h3>Method Not Allowed!</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parser_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))  # 127.0.0.1:5000
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == "__main__":
#     run()


# import sqlite3


# con = sqlite3.connect("profile.db")
# cur = con.cursor()
# cur.execute("""""")
# con.close()

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date BLOB)""")
#     cur.execute("DROP TABLE users")

# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""
#     DROP TABLE person_table
#     """)
#
#     cur.execute("""
#     ALTER TABLE person_table
#     DROP COLUMN home_address
#     """)
#
#     cur.execute("""
#     ALTER TABLE person_table
#     RENAME COLUMN address TO home_address
#     """)
#
#     cur.execute("""
#     ALTER TABLE person_table
#     ADD COLUMN address_add TEXT NOT NULL DEFAULT "Москва";
#     """)
#
#     cur.execute("""
#     ALTER TABLE person
#     RENAME TO person_table;
#     """)
#
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT "+79099000000",
#     age INTEGER CHECK(age > 0 AND age < 100),
#     email TEXT UNIQUE
#     )""")
# import sqlite3
#
# with sqlite3.connect("db_4.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5
#     """)
#
#     # res = cur.fetchall()  # [(), ()]
#     # # res = cur.fetchone()  # ()
#     # # print(res)
#     # # res = cur.fetchmany(10)  # [()]
#     # print(res)
#
#     for res in cur:
#         print(res)


# import sqlite3
#
# cars_list = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
#     cur.execute("UPDATE cars SET price = :Price where model LIKE 'B%'", {'Price': 0})
#
#     cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_list)
#
#     for car in cars_list:
#         cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
#
#     cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
#     cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
#     cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
#     cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
#     cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")


# import sqlite3
#
# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()

# import sqlite3
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost (
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_row_id = cur.lastrowid
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))
#
#     cur.execute("SELECT model, price FROM cars")
#
#     rows = cur.fetchall()
#     rows = cur.fetchone()
#     print(rows)
#     rows = cur.fetchmany(5)
#     print(rows)
#     print()
#
#     for res in cur:
#         print(res[0], res[1])
#         print(res['model'], res['price'])

# import sqlite3
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     )""")
#
#     img = read_ava(1)
#     if img:
#         binary = sqlite3.Binary(img)
#         cur.execute("INSERT INTO users VALUES ('Илья', ?, 1000)", (binary,))
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)

# import sqlite3

# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)


# with sqlite3.connect("car_new.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)


from jinja2 import Template

# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a*2 }} лет. Меня зовут {{ n.upper() }}.")
# msg = tm.render(n=name, a=age)
#
# print(msg)


# per = {"name": "Игорь", "age": 28}
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p['name'] }}.")
# msg = tm.render(p=per)
#
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)

# cities = [
#     {"id": 1, "city": "Москва"},
#     {"id": 2, "city": "Сочи"},
#     {"id": 3, "city": "Смоленск"},
#     {"id": 4, "city": "Ярославль"},
#     {"id": 5, "city": "Минск"}
# ]
#
# link = """
# <select name='cities'>
#     {% for c in cities -%}
#         {% if c.id > 3 -%}
#             <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#         {% elif c.city == "Москва" %}
#             <option>{{ c['city'] }}</option>
#         {% else -%}
#             {{ c['city'] }}
#         {% endif -%}
#     {% endfor -%}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)


# from jinja2 import Template

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]

# tp1 = "{{ (cs | min(attribute='price')).model }}"
# tp1 = "{{ cs | random }}"
# tp1 = "{{ cs | replace('model', 'brand') }}"
# tm = Template(tp1)
# msg = tm.render(cs=cars)
#
# print(msg)
# print(cars)

# html = '''
# {% macro get_input(name, value='', type='text', size=20) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}
#
# <p>{{ get_input('username') }}</p>
# <p>{{ get_input('email') }}</p>
# <p>{{ get_input('password', type='password') }}</p>
# '''
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)


# from jinja2 import Environment, FileSystemLoader

# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0}
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(users=persons, title="About Jinja")
#
# print(msg)

from jinja2 import Environment, FileSystemLoader

subs = ["Культура", "Наука", "Политика", "Спорт"]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(list_table=subs)

print(msg)
