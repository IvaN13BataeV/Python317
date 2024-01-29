k = int(input("Введите число от 1 до 99: "))
if 1 <= k <= 99:
    if 11 <= k <= 14:
        print(k, "копеек")
    else:
        n = k % 10
        if n == 1:
            print(k, "копейка")
        elif 2 <= n <= 4:
            print(k, "копейки")
        else:
            print(k, "копеек")
else:
    print("Выход за допустимый диапазон чисел")
