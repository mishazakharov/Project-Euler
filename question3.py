from math import sqrt
# Simple numbers
simple = []

number = 600851475143
# Находим все делители.
# Не понимаю, почему скрт
for n in range(2,int(sqrt(number)) + 1):
	if number%n == 0:
		# Проверяем каждый делитель на простоту!
		i = 1
		while i != int(sqrt(n)):
			i += 1
			if i != n:
				if n%i == 0:
					i = 0
					break
			else:
				continue
		if i == int(sqrt(n)):
			simple.append(n)

#for n in delitel:


print(simple)

#print(simple[-1])
 