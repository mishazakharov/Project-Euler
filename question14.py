numbers = []
maxlength = 0
chislo = 0
for number in range(500001,1000001,2):
	numbers.append(number)
	while number != 1:
		if number%2 == 0:
			number /= 2
			numbers.append(number)
		else:
			number *= 3
			number += 1
			numbers.append(number)
		if len(numbers) > maxlength:
			maxlength = len(numbers)
			chislo = numbers[0]
	numbers = []

print(chislo,' - ',maxlength)

