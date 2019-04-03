'''
Использовал улучшенный алгоритм факторизации:
Если x*y = number, а y < sqrt(number),то,очевидно,
x > sqrt(number) => любой делитель D0 < sqrt(number)
однозначно связан с D1 > sqrt(number)
Алгоритм выдал правильный результат.
'''
from math import sqrt
result = 0 # Счетчик делителей
for number in range(1,100000):
	if result > 500:
		break
	result = 0 # Обновление количества делителей для каждого нового числа
	x = int((number * (number + 1))/2) # Формирование н-го треугольного числа
	for i in range(1,int(sqrt(x))):
		if x%i == 0:
			result += 2
		if result > 500:
			print(x)
			break



print(result)






