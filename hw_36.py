# 1)
s = 0  # создаем глобальную переменную общей площади до функции


def parallelepiped_area(a, b, c):
    global s  # объявляем глобальной переменной
    s = 2 * (a * b + a * c + b * c)

    def rectangle_area():
        s = a * b

    rectangle_area()  # функция пропускается
    return s


print(parallelepiped_area(2, 4, 6))
print(parallelepiped_area(5, 8, 2))
print(parallelepiped_area(1, 6, 8))
print(s)  # общая площадь из функции записалась в глобальную переменную
print()

# 2)


def parallelepiped_area(a, b, c):
    s = 2 * (a * b + a * c + b * c)

    def top_rectangle_area():
        nonlocal s  # площадь верхнего прямоугольника объявляем нелокальной
        s = a * b

    top_rectangle_area()
    return s


print(parallelepiped_area(2, 4, 6))  # выводится из функции площадь верхнего прямоугольника
print(parallelepiped_area(5, 8, 2))
print(parallelepiped_area(1, 6, 8))
