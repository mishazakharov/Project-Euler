'''
Программа получилась очень долгой,
алгоритм выполняется за (O(sqrt(n**3)).
Посчитал за 3 минуты.

from math import sqrt
numbers = 5
for number in range(1,2000000):
	i = 1
	while i != int(sqrt(number)):
		i += 1
		if number%i != 0:
			if i == int(sqrt(number)) or i == int(sqrt(number))+1:
				numbers += number
				break
			continue
		else:
			break

print(numbers)
'''

# Алгоритм "Решето Эротосфена"!
n = int(2000000)    # число, до которого хотим найти простые числа 
numbers = list(range(2, n + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, n+1, number):
            numbers[candidate-2] = 0    
x = list(filter(lambda x: x != 0, numbers))   # выводим простые числа
print(sum(x))