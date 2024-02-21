def average(func):
    def wrap(*args):
        a = ""
        for i in args:
            a += str(i) + ", "
        print("Среднее арифметическое чисел:", a[:-2], "=", round(func(*args) / len(args), 2))

    return wrap


@average
def summa(*numbers):
    a = ", ".join(map(str, numbers))
    print("Сумма чисел:", a, "=", sum(numbers))
    return sum(numbers)


summa(2, 3, 3, 4)
summa(5, 8, 1, 9, 7, 8, 12)
summa(12, 21, 9, 15, 8, 6, 3, 41, 9, 13)
