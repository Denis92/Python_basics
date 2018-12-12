#author Денис Горшков

import math

def main():
	#Задание №1
	print("Программа для поиска самой большой цифры")
	while True:
		a = input("Введите число:")
		if a.isdigit() :
			print(max(list(a))) 
			break
		else: 
			print("Ошибка: Необходимо было ввести число")
	#Задание №2
	print("\nПрограмма для переопределения переменных")
	a = input("Введите значение переменной а:")
	b = input("Введите значение переменной b:")
	a,b = b,a
	print(f"a = {a} \nb = {b}")
	#Задание №3
	print("\nПрограмма для вычисления корней квадратного уравнения")
	while True:
		a,b,c = input("Введите переменную a:"), input("Введите переменную b:"), input("Введите переменную c:")
		if a.isdigit() and b.isdigit() and c.isdigit():
			a,b,c = int(a), int(b), int(c)
			break
		else:
			print("Ошибка: Одна из переменных содержит символы отличные от числа, повторите ввод")
	D = b**2 - 4 * a * c
	if D >= 0:
		x1 = (-b + math.sqrt(D)) / (2 * a)
		x2 = (-b - math.sqrt(D)) / (2 * a)
		print(f"x1 = {x1} \nx2 = {x2}")
	else:
		print(f"Корней на множестве действительных чисел нет, так как D = {D}")

	input()
if __name__ == '__main__':
	main()