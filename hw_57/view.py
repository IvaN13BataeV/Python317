def add_film(film):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {film} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_film("Редактирование данных каталога фильмов")
    def wait_user_answer(self):
        print("Действия с фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_film("Добавление фильма")
    def add_user_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "имя режиссера": None,
            "год выпуска": None,
            "длительность": None,
            "студию": None,
            "имена актеров": None,
        }
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        print("Фильм добавлен в каталог")
        return dict_film

    @add_film("Каталог фильмов")
    def show_all_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f"{ind}.{film}")

    @add_film("Ввод названия фильма")
    def get_user_title(self):
        user_title = input("Введите название фильма: ")
        return user_title

    @add_film("Просмотр информации о фильме")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} - {film[key]}")

    @add_film("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильм с названием {user_title} отсутствует в каталоге")

    @add_film("Удаление фильма из каталога")
    def remove_single_film(self, film):
        print(f"Фильм {film} - был удален из каталога")

    @add_film("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")