class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Якийсь звук"


class Dog(Animal):

    # def __init__(self, name):

    #     self.name = name

    #

    # def make_sound(self):

    #     return "Якийсь звук"

    def __init__(self, name, breed):
        super().__init__(name)  # Викликаємо конструктор батьківського класу

        self.breed = breed

    def make_sound(self):
        return super().make_sound() + " Гав-гав!"  # Використовуємо метод батьківського класу


# Використання

dog = Dog("Бобік", "Вівчарка")

print(dog.name)  # Виведе: Бобік

print(dog.breed)  # Виведе: Вівчарка

print(dog.make_sound())  # Виведе: Якийсь звук Гав-гав!

