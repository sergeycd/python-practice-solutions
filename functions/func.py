"""Функции для задач."""


def get_index(lst, letter):
    """функция которая возвращает индекс."""
    return lst.index(letter)


def select_value(data, value):
    """Возвращает список элементов."""
    """Элементов превышающих порог, после сортировки
    исходной последовательности по убыванию."""
    new_llist = []
    list_from_tuple = sorted(data, reverse=True)
    for i in list_from_tuple:
        if i > value:
            new_llist.append(i)
        else:
            break
    return new_llist
