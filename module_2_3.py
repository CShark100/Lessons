# Стиль кода часть II. Цикл While.
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_num = 0
while list_num != len(my_list):
    num = my_list[list_num]
    if num > 0:
        print(num)
    elif num < 0:
        break
    list_num += 1

