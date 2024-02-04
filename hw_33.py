physics = {"Максим", "Матвей", "Александр"}
mathematics = {"Матвей", "Евгения", "Михаил", "Максим", "Наталья"}
all_winners = list(physics | mathematics)
print("Все призеры:", all_winners)
both_subjects = physics & mathematics
print("Призеры обеих олимпиад:", both_subjects)
mathematics &= physics
print("Обновленный список призеров по математике:", mathematics)
physics.clear()
