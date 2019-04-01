from math import sqrt
simple = []
for number in range(2,300000):
	i = 0
	while i != int(sqrt(number)):
		i += 1
		if number%i == 0:
			if i == 1:
				continue
			else:
				i = 0
				break
		else:
			continue
	if i == int(sqrt(number)):
		simple.append(number)

def element(simple):
	if simple == []:
		return 0
	else:
		return 30 + element(simple[30:])

kolvo = element(simple)
print(kolvo)
if kolvo > 1000:
	print(simple[10000])