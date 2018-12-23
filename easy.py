
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
	temp_number = float(str(number)[:ndigits + 2])
	get_ndigits_number = int(str(number)[ndigits + 2:ndigits + 3])
	return (temp_number + (1/10 ** ndigits)) if get_ndigits_number >= 5 else temp_number
		


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.9999947, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
	if len(str(ticket_number)) == 6:
		first_number = str(ticket_number)[:len(str(ticket_number))//2]
		second_number = str(ticket_number)[len(str(ticket_number))//2:]
		first_sum = sum(map(lambda x: int(x),first_number))
		second_sum = sum(map(lambda x: int(x),second_number))
		return True if first_sum == second_sum else False
	else:
		return False
		


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
