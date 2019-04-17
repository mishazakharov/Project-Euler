# Все легко

number = 1
for i in range(1,101):
	number *= i

stroka = str(number)
result = 0
for element in stroka:
	result += int(element)

print(result)
