try:
    num_list = []
    n = (int(input("Введите число элементов списка:\nn = ")))
    for i in range(n):
        num = int(input("-> "))
        num_list.append(num)
    print(num_list)
    k = int(input("Введите индекс:\nk = "))
    c = int(input("Введите значение:\nc = "))
    num_list.insert(k, c)
    print(num_list)
except ValueError:
    print("Число введено неверно! Начните вводить заново")


