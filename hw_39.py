while True:
    fio = input("Введите ФИО: ")
    fio_sp = fio.split()
    if len(fio_sp) == 3:
        name = fio_sp[1][:1:], fio_sp[2][:1:], ""
        print(fio_sp[0], ".".join(name))
    else:
        print("Введите 3 слова через пробел")
        continue
    break
