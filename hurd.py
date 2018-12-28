# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли хотя бы один просвет по каждому из трех измерений?
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.
import random
n = 3
def rand_list(n):
	return [round(random.random()) for i in range(n)]
cub = [ [rand_list(n) for i in range(n)] for j in range(n)]
for j in range(len(cub)):
	for i in range(len(cub)):
		temp_re = [cub[k][j][i] for k in range(len(cub))]
		if sum(temp_re) == 0:
			print(f'координаты просвета : x = {i}, y = {j}')
# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.
#
from re import findall
import os

template = r';(\S+)\s*?'
path_pwd = os.path.join('data', 'pwd.txt')
with open(path_pwd, 'r', encoding='UTF-8') as f:
	list_pwd = findall(template , (str(f.readlines()).replace('\\n\',', '')))
set_pwd = set(list_pwd)
list_top_pwd = [[list_pwd.count(i), i] for i in set_pwd ]
sort_top_pwd = sorted(list_top_pwd, reverse = True)[:10]
print('Топ10 самых популярных паролей')
for i in sort_top_pwd:
	print(f'Пароль : {i[1]:>10}, Количество повторений в файле : {i[0]}')
# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами