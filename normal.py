#NORMAL
# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
import os

path = os.path.join('data', 'number.txt')
f = open(path, 'w', encoding='UTF-8')
list_count_num = []
random_num_list = [random.randint(1, 9) for i in range(2500)]
prew = 0
count = 1
for i in random_num_list:
	if i == prew:
		count +=1
	else:
		list_count_num.append([count, prew]) 
		prew = i
		count = 1
list_count_num_sort = sorted(list_count_num, reverse = True)
print(f'Самая длинная последовательность одинаковых цифр: {str(list_count_num_sort[0][1]) * list_count_num_sort[0][0]}')
f.write(f"""{''.join(map(str, random_num_list))}
	Самая длинная последовательность одинаковых цифр: {str(list_count_num_sort[0][1]) * list_count_num_sort[0][0]}""")
f.close()
# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте, остальные элементы тоже рандомные. Пользователь вводит размер
#n = int(input("Введите количество столбцов и столбцов: "))
n = 5
matrix_random = [ [random.randint(0, 100) for i in range(n)] for i in range(n)]
for j in range(n):
	matrix_random[j][random.randint(0, n - 1)] = 0
print(matrix_random)