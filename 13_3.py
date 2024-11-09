""""Паттерн «Фабричный метод»
- Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
- Создайте классы Dog и Cat, которые наследуют от Animal
и реализуют метод speak.
- Создайте класс AnimalFactory, который использует
паттерн «Фабричный метод» для создания экземпляра
Animal. Этот класс должен иметь метод create_animal,
который принимает строку («dog» или «cat») и возвращает
соответствующий объект (Dog или Cat)"""
from abc import ABC, abstractmethod


# Абстрактный класс Animal
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Класс Dog, наследующий от Animal
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"


# Класс Cat, наследующий от Animal
class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"


# Фабрика AnimalFactory, использующая паттерн «Фабричный метод»
class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        """Фабричный метод для создания экземпляра Animal (Dog или Cat)"""
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type. Please choose 'dog' or 'cat'.")


# Пример использования
if __name__ == "__main__":
    factory = AnimalFactory()

    # Создаём собаку
    dog = factory.create_animal("dog")
    print(f"Dog says: {dog.speak()}")

    # Создаём кошку
    cat = factory.create_animal("cat")
    print(f"Cat says: {cat.speak()}")

    # Попытка создания неизвестного животного
    try:
        unknown = factory.create_animal("bird")  # Это вызовет исключение
    except ValueError as e:
        print(e)
