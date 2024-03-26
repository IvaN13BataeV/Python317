class Student:
    def __init__(self, name):
        self.name = name
        self.note = self.Notebook()

    def display_info(self):
        print(self.name, "=>", self.note.info())

    class Notebook:
        model = "HP"
        cpu = "i7"
        ram = 16

        def info(self):
            return f"{self.model}, {self.cpu}, {self.ram}"


student = Student("Роман")
student.display_info()
student = Student("Владимир")
student.display_info()
