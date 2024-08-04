    # Словари и множества
my_dict = {'Serega': 1980, 'Alex': 1978, 'Dima:': 1988}
print('Dict: ', my_dict)                                        # вывод всего словаря
print('Existing value: ', my_dict['Serega'])                    # вывод значения Serega
print('Not existing value: ', my_dict.get('Алиса'))             # вывод отсутствующего значения
my_dict.update ({'Vova': 1982, 'Tim': 1983})                    # добавляем пары
a = my_dict.pop('Alex')                                         # удаляем пару
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)
print()

    # множества
my_set = {1, 'Яблоко', 42.314, 1, 1}                    # присваиваем переменной множество
print('Set: ', my_set)
my_set.update({13, (5, 6, 1.6)})                        # добавляем 2 элемента
my_set.remove(1)                                        # удаляем 1 элемент
print('Modified set: ', my_set)