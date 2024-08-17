# Цикл for. Элементы списка. Полезные функции в цикле

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(2, len(numbers)+1):
    j = 2
    while j * j <= i:
        if i % j == 0:
            not_primes.append(i)
            break
        j += 1
    else:
        primes.append(i)
print('Primes: ', primes)
print('Not primes: ', not_primes)
