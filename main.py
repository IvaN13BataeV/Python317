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


import re

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

s = "12 сентября 2024 года 568789456"
reg = r"\d{2,4}"
print(re.findall(reg, s))

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
