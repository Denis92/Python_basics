#normal
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("fibonacci")
def fibonacci(n, m):
	fibonacci_list = [0]
	fn_1 = 0
	fn_2 = 1
	for x in range(m+1):
		fn = fn_1 + fn_2
		fn_2, fn_1 = fn_1, fn
		fibonacci_list.append(fn)
	return fibonacci_list[n : m + 1]
print(fibonacci(1,10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
	#алгоритм похожий на пузырьковый 
#	for y in range(len(origin_list)-1):
#		min = origin_list[len(origin_list) - y - 1]
#		for k,v in enumerate(origin_list[:len(origin_list) - y]):
#			if min > v:
#				min = v
#				origin_list[len(origin_list) - y - 1], origin_list[k] = v,origin_list[len(origin_list) - y - 1]
#	print(origin_list[::-1])

	#Мой алгоритм
	list_res = []
	for y in origin_list:
		list_res.append(min(origin_list))
		origin_list[origin_list.index(min(origin_list))] = max(origin_list)
	return list_res

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, -13]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(user_function, user_data):
	return [i for i in user_data if user_function(i)]
	
print(my_filter(lambda x: not(x == '8'), '128348858678'))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
#	*--------*
#  *--------*
def check_parallelogramm(x1, y1, x2, y2, x3, y3, x4, y4):
	res_chek = (x2 - x1) == (x4 - x3) and (y1 - y3) == (y2 - y4) and (x1 - x3) == (x2 - x4) and (y2 - y1) == (y4 - y3)
	return res_chek

print(check_parallelogramm(5,5, 10,5, 3,0, 8,0))
