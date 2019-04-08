result = 0
# основание
number = 2
# степень
power = 1000
# возведение в степень
for i in range(1,power):
	number *= 2
# представление числа в строковом виде и подсчет суммы
number = str(number)
for element in number:
	result += int(element)

print(result)