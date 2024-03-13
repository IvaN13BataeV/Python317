class Car:
    def __init__(self, model, release_year, manufacturer, engine_power, color, price):
        self.model = model
        self.release_year = release_year
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, '*'))
        print("Название модели:", self.model)
        print("Год выпуска:", self.release_year)
        print("Производитель:", self.manufacturer)
        print("Мощность двигателя:", self.engine_power)
        print("Цвет машины:", self.color)
        print("Цена:", self.price)
        print(40 * '=')

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_release_year(self, release_year):
        self.release_year = release_year

    def get_release_year(self):
        return self.release_year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine_power(self, engine_power):
        self.engine_power = engine_power

    def get_engine_power(self):
        return self.engine_power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


car = Car("", "", "", "", "", "")
car.print_info()
car.set_model("X7 M50i")
print(car.get_model())
car.set_release_year("2021")
print(car.get_release_year())
car.set_manufacturer("BMW")
print(car.get_manufacturer())
car.set_engine_power("530 л.с.")
print(car.get_engine_power())
car.set_color("white")
print(car.get_color())
car.set_price("10790000")
print(car.get_price())
car.print_info()
