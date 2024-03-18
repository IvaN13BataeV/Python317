class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Имя должно быть строкой!")

    @name.deleter
    def name(self):
        del self.__name

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            print("Возраст должен быть целым числом!")

    @age.deleter
    def age(self):
        del self.__age


pers = Person("Ирина", 26)
print(pers.__dict__)  # первоначальные данные
pers.name = "Игорь"  # изменение имени с проверкой на строку
print(pers.name)
pers.age = 31  # изменение возраста с проверкой на целое число
print(pers.age)
print(pers.__dict__)  # измененные данные имени и возраста
del pers.name
print(pers.__dict__)  # оставшиеся после удаления данные
