class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec < other.sec:
            raise AttributeError("Правый операнд должен быть меньше или равен левому")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec < other.sec:
            raise AttributeError("Правый операнд должен быть меньше или равен левому")
        if other.sec == 0:
            raise ZeroDivisionError("Правый операнд не может быть нулем")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec < other.sec:
            raise AttributeError("Правый операнд должен быть меньше или равен левому")
        if other.sec == 0:
            raise ZeroDivisionError("Правый операнд не может быть нулем")
        return Clock(self.sec % other.sec)

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec > other.sec:
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec < other.sec:
            return True
        return False

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return not self.__gt__(other)


c1 = Clock(180)
c2 = Clock(150)
print(c1.get_format_time())
print(c2.get_format_time())

# 1) Перегрузка операторов: -, -=, *, *=, //, //=, %, %=.

c3 = c1 - c2
print(c3.get_format_time())
# c1 -= c2
# print(c1.get_format_time())
c3 = c1 * c2
print(c3.get_format_time())
# c1 *= c2
# print(c1.get_format_time())
c3 = c1 // c2
print(c3.get_format_time())
# c1 //= c2
# print(c1.get_format_time())
c3 = c1 % c2
print(c3.get_format_time())
# c1 %= c2
# print(c1.get_format_time())

# 2) Перегрузка операторов: >, >=, <, <=

print(c1 > c2)
print(c1 >= c2)
print(c1 < c2)
print(c1 <= c2)
