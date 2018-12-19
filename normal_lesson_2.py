import math
import random

def main():
	print('Задача-1')
	list_num = list(range(100))
	random.shuffle(list_num)
	list_filter = (filter(lambda x: (x >= 0) and (math.sqrt(x) - int(math.sqrt(x)) == 0) ,list_num))
	print(f'Итоговый список: {list(map(lambda x:int(math.sqrt(x)),list_filter))}')

	print('\nЗадача-2')
	dict_number = {
		'01':'певое',
		'02':'второе',
		'03':'третье',
		'04':'четвертое',
		'05':'пятое',
		'06':'шестое',
		'07':'седьмое',
		'08':'восьмое',
		'09':'девятое',
		'10':'десятое',
		'11':'одинадцатое',
		'12':'двенадцатое',
		'13':'тринадцатое',
		'14':'четырнадцатое',
		'15':'пятнадцатое',
		'16':'шеснадцатое',
		'17':'семнадцатое',
		'18':'восемнадцатое',
		'19':'девятнадцатое',
		'20':'двадцатое',
		'30':'тридцатое',
		'31':'тридцать первое'
	}
	dict_month = {
		'01':'января',
		'02':'февраля',
		'03':'марта',
		'04':'апреля',
		'05':'мая',
		'06':'июня',
		'07':'июля',
		'08':'августа',
		'09':'сентября',
		'10':'октября',
		'11':'ноября',
		'12':'декабря',
	}

	strgn_date = '30.12.2010'
	list_date = strgn_date.split('.')
	if 30 > int(list_date[0]) > 20:
		number = f"двадцать {dict_number['0' + str(int(list_date[0]) % 20)]}"
	else:
		number = dict_number.get(list_date[0])
	print(f'{number} {dict_month.get(list_date[1])} {list_date[2]} года' )

	print('\nЗадача-3')
	n = 100
	list_num = [random.randint(-100,100) for i in range(n)]
	print(f'Список случайных чисел: {list_num}')
if __name__ == '__main__':
	main()