from math import sqrt


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def change_num(self, new_a, new_b):
        self.a = new_a
        self.b = new_b

    def prod_num(self):
        return self.a * self.b

    def summ_num(self):
        return self.a + self.b


class RightTriangle(Pair):
    def hypotenuse(self):
        return round(sqrt(self.a ** 2 + self.b ** 2), 2)

    def area(self):
        return self.a * self.b / 2


rt = RightTriangle(5, 8)  # создаем экземпляр дочернего класса
print(f"Гипотенуза АВС: {rt.hypotenuse()}")
print(f"Прямоугольный треугольник АВС ({rt.a}, {rt.b}, {rt.hypotenuse()})")
print(f"Площадь АВС: {rt.area()}")
print()
print(f"Сумма: {rt.summ_num()}")
print(f"Произведение: {rt.prod_num()}")
print()
rt.change_num(10, 20)  # меняем числа через метод родительского класса
print(f"Гипотенуза АВС: {rt.hypotenuse()}")
print(f"Сумма: {rt.summ_num()}")
print(f"Произведение: {rt.prod_num()}")
print(f"Площадь АВС: {rt.area()}")
