from math import pi, sqrt

print("Вычисление площади фигуры")
try:
    f = input("Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - круг\n: ")
    if f == '1':
        a = int(input("Введите сторону a: "))
        b = int(input("Введите сторону b: "))
        c = int(input("Введите сторону c: "))
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        print("Площадь треугольника:", round(s, 2))
    elif f == '2':
        a = int(input("Введите сторону a: "))
        b = int(input("Введите сторону b: "))
        s = a * b
        print("Площадь прямоугольника:", s)
    elif f == '3':
        r = int(input("Введите радиус: "))
        s = pi * r ** 2
        print("Площадь круга:", round(s, 2))
    else:
        print("Фигура выбрана неверно!")
except ValueError:
    print("Неверный ввод целого числа!")
