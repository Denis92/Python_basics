#EASY
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
list_input = [1, 2, 4, 0]
print([i**2 for i in list_input])

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
list_fruts_first = ['яблоки', 'апельсины', 'бананы', 'абрикосы', 'персики', 'киви']
list_fruts_second = ['яблоки', 'ананасы', 'бананы', 'абрикосы', 'персики', 'киви', 'гранат', 'виноград']
list_fruts_res = [j for i in list_fruts_first for j in list_fruts_second if i == j]
print(list_fruts_res)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random

list_random = [ random.randint(-100, 100) for i in range(100)]
list_res = [i for i in list_random if (i > 0) and (i % 3 == 0) and (i % 4 != 0)]
print(list_res)
