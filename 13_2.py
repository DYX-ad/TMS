"""Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions,
bacon.
- Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
- Создайте класс PizzaDirector, который принимает
экземпляр PizzaBuilder и содержит метод make_pizza,
который использует PizzaBuilder для создания Pizza
"""
# Класс Pizza
class Pizza:
    def __init__(self, size=None, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        ingredients = [
            "cheese" if self.cheese else "",
            "pepperoni" if self.pepperoni else "",
            "mushrooms" if self.mushrooms else "",
            "onions" if self.onions else "",
            "bacon" if self.bacon else ""
        ]
        ingredients = ", ".join(filter(None, ingredients))
        return f"Pizza (Size: {self.size}, Ingredients: {ingredients})"


# Класс PizzaBuilder (Строитель)
class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def set_size(self, size):
        self._pizza.size = size
        return self

    def add_cheese(self):
        self._pizza.cheese = True
        return self

    def add_pepperoni(self):
        self._pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self._pizza.mushrooms = True
        return self

    def add_onions(self):
        self._pizza.onions = True
        return self

    def add_bacon(self):
        self._pizza.bacon = True
        return self

    def build(self):
        return self._pizza


# Класс PizzaDirector (Директор)
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        # Пример комплексной пиццы с несколькими ингредиентами
        return (self.builder
                .set_size("Large")
                .add_cheese()
                .add_pepperoni()
                .add_mushrooms()
                .build())

""""Использование"""
# Создаём экземпляр PizzaBuilder
builder = PizzaBuilder()

# Создаём PizzaDirector и заказываем пиццу через метод make_pizza
director = PizzaDirector(builder)
pizza = director.make_pizza()

print(pizza)  # Результат: Pizza (Size: Large, Ingredients: cheese, pepperoni, mushrooms)