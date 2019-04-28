
# Хранит избыточные числа!...
overs = []
allset = set()

# Хранит сумму Сигма n
peremennaia = 0
for number in range(1,28124):
	allset.add(number)
	summ = 0
	for delitel in range(1,number):
		if number%delitel == 0:
			summ += delitel
	if summ > number:
		overs.append(number)

numbers = set()

for number in overs:
	for number1 in overs:
		summ1 = number + number1
		numbers.add(summ1)

result = allset - numbers
print(sum(result))



