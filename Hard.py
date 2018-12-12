#author Денис Горшков

def main():
	#Задание №1
	print("Программа для определения простого числа")
	strngount = 0
	while True:
		user_number = input("Введите число:")
		if user_number.isdigit():
			user_number = int(user_number)
			break
		else:
			print("Ошибка: Был введён символ отличный от цифры")

	for i in range(1 , user_number + 1):
		if user_number % i == 0:
			strngount += 1
	if strngount <= 2:
		print(f"Число {user_number} является простым")
	else:
		print(f"Число {user_number} не является простым так как делится, кроме 1 и самого себя ещё на следующее количество чисел: {strngount - 2}")

	#Задание №2
	print("\nПрограмма для вычисления числа Фибоначчи")
	fn_1 = 0
	fn_2 = 1
	while True:
		n = input("Введите число n:")
		if n.isdigit():
			n = int(n)
			break
		else:
			print("Ошибка: Был введён символ отличный от цифры")

	for x in range(n):
		fn = fn_1 + fn_2
		fn_2, fn_1 = fn_1, fn
	print(f"Число Фибоначчи при n = {n}\nРавно: {fn}")
	#Задание №3
	print("\nПрограмма для формирования строк")
	while True:
		n = input("Введите число строк:")
		m = input("Введите число троек 'AAA':")
		if n.isdigit() and m.isdigit():
			n = int(n)
			m = int(m)
			break
		else:
			print("Ошибка: Был введён символ отличный от цифры")

	strng = "AAA"
	for x in range(1,m):
		strng += "BBBAAA"

	for x in range(1,n + 1):
		if x % 2 != 0:
			print(f"{strng}BBB")
		else:
			print(f"BBB{strng}")

	input()
if __name__ == '__main__':
	main()
