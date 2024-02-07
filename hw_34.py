sales = {
    'John': {
        'N': 3056,
        'S': 8463,
        'E': 8441,
        'W': 2694
    },
    'Tom': {
        'N': 4832,
        'S': 6786,
        'E': 4737,
        'W': 3612
    },
    'Anne': {
        'N': 5239,
        'S': 4882,
        'E': 5820,
        'W': 1859
    },
    'Fiona': {
        'N': 3984,
        'S': 3645,
        'E': 8821,
        'W': 2451
    }
}
for i in sales:
    print(i)
    for j in sales[i]:
        print(j, ":", sales[i][j])

while True:
    name = input("Имя: ")
    if name in sales:
        while True:
            region = input("Регион: ")
            if region in sales[name]:
                print("Объем продаж:", sales[name][region])
                while True:
                    try:
                        new_value = int(input("Новое значение: "))
                        sales[name][region] = new_value
                        print(sales[name])
                        break
                    except ValueError:
                        print("Значение некорректное. Введите число!")
            else:
                print("Регион введен неверно!")
                continue
            break
    else:
        print("Такое имя отсутствует!")
        continue
    break

