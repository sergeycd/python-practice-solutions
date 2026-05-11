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

# Создайте список basket с тремя овощами: 'Помидоры', 'Огурцы', 'Кабачки'.
# Выполните последовательно следующие действия:

# Добавьте в конец списка 'Баклажаны'.

# Вставьте на вторую позицию (индекс 1) 'Перец'.

# Удалите из списка 'Огурцы' (используйте метод remove).

# Удалите последний элемент списка и сохраните его в переменную
# last_vegetable (используйте pop).

# После каждого шага печатайте список, чтобы видеть изменения. В конце
# выведите значение переменной last_vegetable.

# Ожидаемый итоговый список: ['Помидоры', 'Перец', 'Кабачки']
# В переменной last_vegetable: 'Баклажаны'

basket = ['Помидоры', 'Огурцы', 'Кабачки']
print(basket)
basket.append('Баклажаны')
print(basket)
basket.insert(1, 'Перец')
print(basket)
basket.remove('Огурцы')
print(basket)
last_vegetable = basket.pop(-1)
print(basket)
print(last_vegetable)

# Дан список урожайности:
# yields = [10, 12, 15, 10, 8, 10]
# Создайте настоящую копию этого списка в переменной true_copy с помощью метода copy.
# Создайте переменную fake_copy и присвойте ей значение yields.
# Отсортируйте исходный список yields по возрастанию.
# Выведите на экран yields, true_copy и fake_copy.
# Объясните (в комментарии) почему вывод true_copy и fake_copy различается.

yields = [10, 12, 15, 10, 8, 10]
true_copy = yields.copy()
fake_copy = yields
yields.sort()
print(yields)
print(true_copy)
print(fake_copy)
# Отличие заключается в том что данные списки стали разными сущностями в тот
# момент когда
# мы создали копию исходного списка через метод copy


# Дан список урожайности овощей за неделю:
# harvest = [5, 12, 8, 12, 15, 8, 10]
# Выполните следующие действия и зафиксируйте результаты:
# Сколько раз в списке встречается значение 12?
# Сохраните ответ в переменную count_12.
# На каком месте (индекс) впервые встречается значение 8?
# Сохраните в first_8_index.
# Отсортируйте список по возрастанию, а затем разверните его
# (сделайте сортировку по убыванию,
# используя комбинацию sort и reverse).
# Найдите и сохраните в переменную last_harvest последний элемент
# отсортированного
# по убыванию списка (то есть самый маленький урожай), используя
# pop без аргументов.
# Выведите все полученные переменные: count_12, first_8_index,
# отсортированный по убыванию список и last_harvest.
# Ожидаемый результат:
# count_12 → 2
# first_8_index → 2
# Отсортированный по убыванию список → [15, 12, 12, 10, 8, 8, 5]
# last_harvest → 5

harvest = [5, 12, 8, 12, 15, 8, 10]
count_12 = harvest.count(12)
print(count_12)
first_8_index = harvest.index(8)
print(first_8_index)
harvest.sort()
print(harvest)
harvest.reverse()
print(harvest)
last_harvest = harvest.pop()
print(last_harvest)
