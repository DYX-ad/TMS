"""Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три числа,
другой объект класса MyTime, и отсутствие входных параметров. Реализовать
нормальное отображение времени
"""
class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        """ Конструктор, поддерживающий передачу трёх чисел.
        Если параметры не заданы, время по умолчанию 0:0:0.
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        """ Нормализация времени: перевод секунд и минут в диапазон 0-59. """
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60

    def __str__(self):
        """ Простой вывод времени в формате hh:mm:ss """
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __eq__(self, other):
        """ Проверка равенства двух объектов MyTime """
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def __lt__(self, other):
        """ Проверка, меньше ли текущее время другого """
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)

    def __add__(self, other):
        """ Сложение двух объектов MyTime """
        return MyTime(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def __sub__(self, other):
        """ Вычитание двух объектов MyTime """
        total_seconds = self.to_seconds() - other.to_seconds()
        if total_seconds < 0:
            total_seconds = 0  # Чтобы результат не был отрицательным
        return MyTime.from_seconds(total_seconds)

    def __mul__(self, factor):
        """ Умножение времени на целое число """
        return MyTime.from_seconds(self.to_seconds() * factor)

    def to_seconds(self):
        """ Переводит время в общее количество секунд """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        """ Создаёт объект MyTime из общего числа секунд """
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)


# Пример использования:
t1 = MyTime(2, 45, 90)   # Создание объекта с нормализацией
t2 = MyTime(1, 20, 45)   # Создание второго объекта
t3 = t1 + t2                                    # Сложение объектов времени
t4 = t1 - t2                                    # Вычитание объектов времени
t5 = t1 * 2                                     # Умножение времени на число

print("Время t1:", t1)
print("Время t2:", t2)
print("Сложение t1 + t2:", t3)
print("Вычитание t1 - t2:", t4)

