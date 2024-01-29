try:
    n = [float(input("Введите число: ")) for i in range(int(input("Введите количество чисел в последовательности: ")))]
    min_n = max_n = n[0]
    summ = 0
    for i in n:
        if i < min_n:
            min_n = i
        if i > max_n:
            max_n = i
        summ += i
    res = summ / len(n)
    print("Количество чисел:", len(n))
    print("Среднее арифметическое:", round(res, 2))
    print("Наименьшее число:", min_n)
    print("Наибольшее число:", max_n)
except ValueError:
    print("Ошибка ввода числа! Повторите попытку заново")
else:
    print("Список введенных чисел:", n)
finally:
    print("Работа программы завершена...")
