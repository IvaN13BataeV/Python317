def average(func):
    def wrap(*args):
        print(func(*args))
        return f"Среднее арифметическое чисел: {round(func(*args) / len(args), 2)}"

    return wrap


@average
def summa(*numbers):
    return sum(numbers)


print(summa(2, 3, 3, 4))
print(summa(5, 8, 1, 9, 7, 8, 12))
print(summa(12, 21, 9, 15, 8, 6, 3, 41, 9, 13))
