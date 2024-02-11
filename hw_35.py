while True:
    try:
        n = int(input("Количество студентов: "))
        students = []
        scores = []
        for i in range(n):  # создаем списки студентов и их оценок
            student = input(str(i + 1) + "-й студент: ")
            students.append(student)
            while True:
                try:
                    score = int(input("Балл: "))
                    if 1 <= score <= 12:
                        scores.append(score)
                    else:
                        print("Введите балл от 1 до 12")
                        continue
                except ValueError:
                    print("Ошибка ввода числа!")
                    continue
                break
        average = sum(scores) // len(scores)  # вычисляем средний балл
        dict_scores = dict(zip(students, scores))  # создаем словарь из списков
        print("Средний балл:", average)
        print("Студенты с баллом выше среднего:")
        for student in dict_scores:  # выводим требуемых студентов из словаря
            if dict_scores[student] > average:
                print(student)
    except ValueError:
        print("Ошибка ввода числа!")
        continue
    break
