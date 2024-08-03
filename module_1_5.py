# Неизменяемые и изменяемые объекты. Кортежи
immutable_var = 1, 2, True, "String"
print("Immutable tuple: ", immutable_var)
# immutable_var[0] = 200                        # попытка изменить элемент выдаст ошибку
# кортеж – это неизменяемая упорядоченная коллекция, которая может содержать в себе разные типы данных

mutable_list = ['apple', 'coconut', 'banana']
print("Normal list: ", mutable_list)            # вывод списка
mutable_list[1] = 'peach'                       # замена в списке
print("Mutable list: ", mutable_list)           # вывод списка с заменой