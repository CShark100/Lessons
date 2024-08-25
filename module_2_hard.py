# Задание "Слишком древний шифр"
def result(n):
    pass_ = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0 and n > 2 and n < 21:
                pass_ += str(i) + str(j)
    return pass_
print('Введите число от 3 до 20: ')
print(result(int(input())))