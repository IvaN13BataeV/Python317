from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side ** 2

    def draw(self):
        for i in range(self.side):
            print('*' * self.side)

    def info(self):
        return (f"===Квадрат===\nСторона: {self.side}\nЦвет: {self.color}\nПлощадь: {self.area()}"
                f"\nПериметр: {self.perimeter()}")


class Rectangle(Shape):
    def __init__(self, color, side1, side2):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2

    def perimeter(self):
        return self.side1 * 2 + self.side2 * 2

    def area(self):
        return self.side1 * self.side2

    def draw(self):
        for i in range(self.side1):
            print('*' * self.side2)

    def info(self):
        return (f"===Прямоугольник===\nДлина: {self.side1}\nШирина: {self.side2}\nЦвет: {self.color}"
                f"\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}")


class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        p = self.perimeter() / 2
        return round(sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)), 2)

    def draw(self):
        for i in range(1, 7):
            spaces = " " * (6 - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)

    def info(self):
        return (f"===Треугольник===\nСторона 1: {self.side1}\nСторона 2: {self.side2}\nСторона 3: {self.side3}\n"
                f"Цвет: {self.color}\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}")


sq = Square("red", 3)
rect = Rectangle("green", 3, 7)
tr = Triangle("yellow", 11, 6, 6)

for shape in (sq, rect, tr):
    print(shape.info())
    shape.draw()
    print()
