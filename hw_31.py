print("Частотность символов в кортеже.")

t = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
while ' ' in t:
    print("Введен пробел!", end=" ")
    t = tuple(input("Введите заново без пробелов элементы кортежа: "))
else:
    print(t)
    l = []
    for i in t:
        if i not in l:
            l.append(i)
            print("Количество '" + i + "' =", t.count(i))
