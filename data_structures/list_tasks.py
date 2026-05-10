"""Здачи по спискам."""
import sys
from pathlib import Path

if __name__ == '__main__':
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import init_path
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
