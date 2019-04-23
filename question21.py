counts = set()
numbers = [number for number in range(0,10000)]
for number in numbers:
	c = 0
	for i in range(1,number):
		if number%i == 0:
			c += i
	#print('Сумма делителей числа',number,':',c)
	d = 0
	for b in range(1,c):
		if c%b == 0:
			d += b
	#print('\tСумма делителей числа',c,':',d)

	if number == d:
		if number != c:
			counts.add(number)
			counts.add(c)

			#print('Добавил',number,c)
print(sum(counts))