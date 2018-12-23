#hurd
# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
from re import findall

def check_int(input_list):
	for i in range(len(input_list)):
		if input_list[i] == "":
			input_list[i] = '1'
	return input_list

def decimal_func(str_decimal):
	template = r'-?[\w]+/?[\w]?\s*?(\+|\-)\s*?-?[\w]+/?[\w]?'
	sign_expression = list(findall(template, str_decimal))
	template = r'(\-?\w+)/?(\w+)?'
	list_numbers = findall(template,str_decimal)
	first_number = list(map(int, check_int(list(list_numbers[0]))))
	second_number = list(map(int, check_int(list(list_numbers[1]))))
	denominator = first_number[1] * second_number[1] 
	if sign_expression[0] == '-':
		numerator = first_number[0] * second_number[1] - second_number[0] * first_number[1]
	if sign_expression[0] == '+':
		numerator = first_number[0] * second_number[1] + second_number[0] * first_number[1]
	if numerator == 0:
		return "result = 0"
	divisor_numerator = set(filter(lambda x: abs(numerator) % int(x) == 0 ,range(1,abs(numerator) + 1)))
	divisor_denominator = set(filter(lambda x: denominator % int(x) == 0 ,range(1,denominator + 1)))
	common_divisor_max = (max(divisor_numerator.intersection(divisor_denominator)))
	if numerator >= denominator:
		int_num  = numerator // denominator
		numerator -=  int_num * denominator
		return f'result = {int_num}'if numerator == 0 else f'result = {int_num} {numerator // common_divisor_max}/{denominator // common_divisor_max}'
	else:
		return f'result = {numerator // common_divisor_max}/{denominator // common_divisor_max}'

print(decimal_func('-4/5 - -2/5'))
print(decimal_func('4/5 - -2/5'))
print(decimal_func('4/5 - -2'))
print(decimal_func('4 - -2'))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os

path_workers = os.path.join('data', 'workers.txt')
path_hours = os.path.join('data', 'hours_of.txt')
f_workers = open(path_workers, 'r', encoding='UTF-8')
f_hours = open(path_hours, 'r', encoding='UTF-8')
template_workers = r'([а-яА-Я]+\s*?[а-яА-Я]+)\s*?([0-9]+)\s*?([а-я]+)\s*?([0-9]+)'
template_hours = r'([а-яА-Я]+\s*?[а-яА-Я]+)\s*?([0-9]+)'

with open(path_workers, 'r', encoding='UTF-8') as f_workers:
	find_workers = findall(template_workers, str(f_workers.readlines()))
with open(path_hours, 'r', encoding='UTF-8') as f_hours:
	find_hours = findall(template_hours, str(f_hours.readlines()))
list_join = []
for j in range(len(find_workers)):
	for i in range(len(find_hours)):
		if find_hours[i][0] in find_workers[j][0]:
			list_join.append([find_workers[j][0], find_workers[j][1], find_workers[j][3], find_hours[i][1]])
for i in range(len(list_join)):
	ratio = int(list_join[i][1])/int(list_join[i][2])
	difference = int(list_join[i][3]) - int(list_join[i][2])
	selori = int(list_join[i][1])
	if difference < 0:
		res_selori = selori + difference * ratio
	else:
		res_selori = selori + 2 * difference * ratio
	print(f'{list_join[i][0]}: {res_selori}')
# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

def funct(list_letters, list_words):
    for i in list_letters:
    	res = list(filter(lambda x: i in x, list_words))
    	if res:
    		path = os.path.join('data', f'fruits_{i}.txt')
    		new_f = open(path, 'w', encoding='UTF-8')
    		for num, words in enumerate(res):
    			new_f.write(f'{num}: {words}\n')
    		new_f.close()
def fruits_file():
	path = os.path.join('data', 'fruits.txt')
	f = open(path, 'r', encoding='UTF-8')
	template = r'([а-яА-Яa-zA-Z]+\s*?[а-яa-z]+)'
	with open(path, 'r', encoding='UTF-8') as f:
	    list_words = findall(template,str(f.readlines()))
	    list_rus_letters = list(map(chr, range(ord('А'), ord('Я')+1)))
	    list_en_letters = list(map(chr, range(ord('A'), ord('Z')+1)))
	    print(list_words)
	    funct(list_rus_letters, list_words)
	    funct(list_en_letters, list_words)

