import random
def main():
	print('Задача-1')
	list_input = ["яблоко", "банан", "киви", "арбуз"]
	for count in range(len(list_input)):
		print(f"{count + 1}. {list_input[count]:>6}")

	print('\nЗадача-2')
	list_first = list(range(100))
	list_second = list(range(50,100,2))
	print(f'Отфильтрованый список: {list(filter(lambda x: not(x in list_second),list_first))}')

	print('\nЗадача-3')
	list_num = list(range(100))
	random.shuffle(list_num)
	list_new = [(x / 4) if x % 2 == 0 else (x * 2) for x in list_num]
	print(f'Новый список :{list_new}')
	
if __name__ == '__main__':
	main()