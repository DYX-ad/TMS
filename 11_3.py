"""Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
- метод is_repeatance(s), который принимает некоторую
строку и возвращает True или False в зависимости от того,
может ли текущая строка быть получена целым
количеством повторов строки s. Считать, что пустая
строка не содержит повторов
- метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом.
"""
class SuperStr(str):
    def is_repeatance(self, s):
        """Проверяет, можно ли текущую строку получить путём повторения строки s."""
        if not s:  # Пустая строка не имеет повторов
            return False
        # Проверяем, делится ли длина текущей строки на длину строки s
        repeat_count = len(self) // len(s)
        return s * repeat_count == self

    def is_palindrom(self):
        """Проверяет, является ли строка палиндромом (без учёта регистра)."""
        # Приводим строку к нижнему регистру и проверяем, равна ли она своему обращению
        normalized_str = self.lower()
        return normalized_str == normalized_str[::-1]


# Примеры использования
s1 = SuperStr("abcabcabc")
print(s1.is_repeatance("abc"))  # True
print(s1.is_repeatance("ab"))    # False

s2 = SuperStr("madam")
print(s2.is_palindrom())         # True

s3 = SuperStr("hello")
print(s3.is_palindrom())         # False

s4 = SuperStr("")
print(s4.is_palindrom())         # True (пустая строка считается палиндромом)
