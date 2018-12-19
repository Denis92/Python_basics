import string

def text_user(text):
	text = text.lower()
	text = ''.join(list(filter(lambda x: not(x in list(string.punctuation)),list(text))))
	return text.split(" ")

def main():
	print('Задача-1')
	text = "This functions drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(), passing args and kws straight through. By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments. In this case, it is purely a convenience function so you don’t have to explicitly import pdb or type as much code to enter the debugger. However, sys.breakpointhook() can be set to some other function and breakpoint() will automatically call that, allowing you to drop into the debugger of choice."
	words = text_user(text)
	list_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'l', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	print(f'Количество слов: {len(words)}')
	count_w = len(list(filter(lambda x: x in list_en, list(text.replace(' ','')))))
	print(f'Количество букв английского алфавита в тексте: {count_w}')


	print('\nЗадача-2')
	text_1 = "This function drops you into the debugger at the call site. However, sys.breakpointhook() can be set"
	words_1 = text_user(text_1)
	text_2 = "This function drops you into the debugger at the call site. Specifically, it calls sys.breakpointhook(), passing args and kws straight through. By default, sys.breakpointhook() calls pdb.set_trace() expecting no arguments. In this case, it is purely a convenience function so you don’t have to explicitly import pdb or type as much code to enter the debugger. However, sys.breakpointhook() can be set to some other function and breakpoint() will automatically call that, allowing you to drop into the debugger of choice."
	words_2 = text_user(text_2)
	print('Список уникальных пересечений слов в обоих текстах ')
	list_same_words = list(filter(lambda x: x in set(words_1), set(words_2)))
	for count in range(len(list_same_words)):
		print(f"{(count + 1):<2} {list_same_words[count]}")
if __name__ == '__main__':
	main()