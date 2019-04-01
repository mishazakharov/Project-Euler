# Определение двух взаимно простых чисел(теорема Евклида!).
# Работает не совсем так, как задумано!
numbers = []
for first in range(2,100):
	delitel1 = set()
	for number1 in range(2,first):
		if first%number1 == 0 and first != number1:
			delitel1.add(number1)
	for second in range(2,100):
		delitel2 = set()
		for number2 in range(2,second):
			if second%number2 == 0 and second != number2:
				delitel2.add(number2)
		split = delitel1 & delitel2
		if not split:
			kortej = (first,second)
			numbers.append(kortej)
'''
 Создание пифагоровй тройки из двух взаимно простых чисел(по теореме Евклида!).
 Если сумма элементов тройки равняется заданному числу(1000),
 то выводится кортеж тройки и сообщение!
 Вся программа работает не совсем так, как было задумано,но
 она решает поставленную и многие другие задачи.
'''
for element in numbers:
	if sum(kortej) == 1000:
		break
	if element[0] > element[1]:
		m = element[0]
		n = element[1]
	else:
		m = element[1]
		n = element[0]
	while m != 1000 and n != 1001:
		a = m**2 - n**2
		b = 2*m*n
		c = m**2 + n**2
		kortej = (a,b,c)
		if sum(kortej) == 1000:
			print('We found him!',kortej)
			break
		m += 1
		n += 1

