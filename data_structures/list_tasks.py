"""Здачи по спискам."""
import sys
from pathlib import Path

if __name__ == '__main__':
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from functions.func import get_index

# Дан список букв из названия фильма:

# python
# movie_name_sequence = ['Д', 'ж', 'о', 'н', 'н', 'и', ' ', 'М', 'н', 'е',
# 'м', 'о', 'н', 'и', 'к']
# Напишите код, который выведет на экран слово «жми», составленное из
# элементов этого списка.
# Используйте только обращение по индексам и функцию print(). Каждая буква —
# отдельный вызов print()
# (чтобы каждая буква оказалась на новой строке).

# Ожидаемый вывод:
# ж
# м
# и

movie_name_sequence = ['Д', 'ж', 'о', 'н', 'н', 'и', ' ', 'М', 'н', 'е', 'м',
                       'о', 'н', 'и', 'к']

first_letter, second_letter, third_letter = [
    movie_name_sequence[get_index(movie_name_sequence, 'ж')],
    movie_name_sequence[get_index(movie_name_sequence, 'м')],
    movie_name_sequence[get_index(movie_name_sequence, 'и')]
    ]
print(first_letter)
print(second_letter)
print(third_letter)

# В списке apples_by_day хранятся данные об урожае яблок за 10 дней:
# apples_by_day = [61, 58, 56, 34, 67, 50, 74, 64, 78, 69]
# Распакуйте этот список в отдельные переменные, дав им осмысленные имена
# (например, day1, day2, … или mon, tue, …).
# Затем вычислите и напечатайте сумму яблок за первые три дня и сумму яблок за
# последние три дня, используя только полученные переменные (без обращения к
# исходному списку).

apples_by_day = [61, 58, 56, 34, 67, 50, 74, 64, 78, 69]
day1, day2, day3, day4, day5, day6, day7, day8, day9, day10 = apples_by_day
print(day1 + day2 + day3)
print(day8 + day9 + day10)
