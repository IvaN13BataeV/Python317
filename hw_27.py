try:
    lst = []
    n = int(input("Введите количество элементов списка: "))
    for i in range(n):
        x = int(input("Введите число кратное 3: "))
        if x % 3 == 0:
            lst.append(x)
        else:
            print(x, "не делится на 3 без остатка!")
except ValueError:
    print("Число введено неверно! Повторите попытку ввода")
else:
    print("Список введенных чисел кратных 3:", lst)
