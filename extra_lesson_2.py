def main():
#Ввод информации
#	print('Для завершения ввода, напишите ключевое слово end')
#	dict_recipe = {}
#	while True:
#		k, v = input("Ведите наименование необходимого продукта: "), input("Ведите количество данного продукта: ")
#		if k == "end" or v == "end":
#			break
#		dict_recipe[k] = v
#	print(dict_recipe)

#	dict_refrigiration = {}
#	while True:
#		k, v = input("Ведите наименование имеющегося продукта: "), input("Ведите количество данного продукта: ")
#		if k == "end" or v == "end":
#			break
#		dict_refrigiration[k] = v
#	print(dict_refrigiration)

	dict_recipe = {
		'bacon' : 250,
		'carrot' : 1,
		'potato' : 4,
		'green_pea' : 1,
		'cucumbers' : 4,
		'onion' : 1,
		'boiled_egg' : 4,
		'mayonnaise' : 150
		}
	dict_refrigiration = {
		'bacon' : 250,
		'carrot' : 1,
		'potato' : 4,
		'green_pea' : 1,
		'cucumbers' : 4,
		'onion' : 1,
		'boiled_egg' : 4,
		#'mayonnaise' : 150
		}
	dict_need = {k : (dict_recipe.get(k) - dict_refrigiration.setdefault(k,0)) for k,v in dict_recipe.items() if (dict_recipe.get(k) - dict_refrigiration.setdefault(k,0))}
	print('Все продукты присутствуют в нужных количествах') if len(dict_need) == 0 else print(f'Необходимо купить{dict_need}')
if __name__ == '__main__':
	main()