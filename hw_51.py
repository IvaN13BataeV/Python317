class ValidCoord:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} должно быть целым числом")
        setattr(instance, self.name, value)


class Point3D:
    x = ValidCoord()
    y = ValidCoord()
    z = ValidCoord()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


point = Point3D(0, 0, 0)
# point.x = "1"  # вводим строку для проверки дескриптора
# point.y = 2.3 # вводим вещественное число для проверки дескриптора
point.x = 1
point.y = 2
point.z = 3
print(point.__dict__)
