from math import pi

print("Вычисление площади фигуры")

try:
    def get_rectangle_area():
        a = int(input("Длина: "))
        b = int(input("Ширина: "))
        print("Площадь прямоугольника:", a * b)


    def get_triangle_area():
        a = int(input("Основание: "))
        h = int(input("Высота: "))
        print("Площадь треугольника:", a * h / 2)


    def get_circle_area():
        r = int(input("Радиус: "))
        print("Площадь круга:", round(pi * r ** 2, 2))

    figure = input("Фигура:\n1 - прямоугольник, 2 - треугольник, 3 - круг\n: ")
    if figure == '1':
        get_rectangle_area()
    elif figure == '2':
        get_triangle_area()
    elif figure == '3':
        get_circle_area()
    else:
        print("Фигура выбрана неверно!")
except ValueError:
    print("Целое число введено неверно!")
