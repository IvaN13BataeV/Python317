# 1)
s = 0  # создаем глобальную переменную общей площади до функции


def parallelepiped_area(a, b, c):
    def rectangle_area(side1, side2):
        return side1 * side2

    global s  # объявляем глобальной переменной
    s = 2 * (rectangle_area(a, b) + rectangle_area(a, c) + rectangle_area(b, c))
    return s


print(parallelepiped_area(2, 4, 6))
print(parallelepiped_area(5, 8, 2))
print(parallelepiped_area(1, 6, 8))
print(s)  # общая площадь из функции записалась в глобальную переменную
print()

# 2)


def parallelepiped_area(a, b, c):
    def rectangle_area(side1, side2):
        return side1 * side2

    s = 2 * (rectangle_area(a, b) + rectangle_area(a, c) + rectangle_area(b, c))
    return s


print(parallelepiped_area(2, 4, 6))
print(parallelepiped_area(5, 8, 2))
print(parallelepiped_area(1, 6, 8))
