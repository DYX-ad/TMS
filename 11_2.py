"""Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость
(по умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость  - 5), стоп (сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные. Сделать для
каждого атрибута getter и setter используя декораторы/
"""
class Car:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = 0  # Скорость по умолчанию

    # Геттеры и сеттеры для атрибутов с использованием декораторов
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value >= 0:
            self._speed = value
        else:
            raise ValueError("Скорость не может быть отрицательной.")

    # Методы для изменения состояния машины
    def increase_speed(self):
        """Увеличение скорости на 5."""
        self._speed += 5

    def decrease_speed(self):
        """Уменьшение скорости на 5, не опуская её ниже нуля."""
        self._speed = max(0, self._speed - 5)

    def stop(self):
        """Сброс скорости на 0."""
        self._speed = 0

    def display_speed(self):
        """Отображение текущей скорости."""
        print(f"Текущая скорость: {self._speed} км/ч")

    def reverse(self):
        """Разворот - изменение знака скорости."""
        self._speed = -self._speed if self._speed != 0 else 0

# Пример использования
my_car = Car("Toyota", "Camry", 2020)
my_car.increase_speed()
my_car.display_speed()  # Выводит: Текущая скорость: 5 км/ч
my_car.increase_speed()
my_car.display_speed()  # Выводит: Текущая скорость: 10 км/ч
my_car.decrease_speed()
my_car.display_speed()  # Выводит: Текущая скорость: 5 км/ч
my_car.reverse()
my_car.display_speed()  # Выводит: Текущая скорость: -5 км/ч
my_car.stop()
my_car.display_speed()  # Выводит: Текущая скорость: 0 км/ч

