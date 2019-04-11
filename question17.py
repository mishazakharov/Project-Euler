import inflect

result = 0

p = inflect.engine()
for number in range(1,1000):
	i = ''
	time = p.number_to_words(number)
	if number <= 20:
		result += len(time)
	elif number == 30:
		result += len(time)
	elif number == 40:
		result += len(time)
	elif number == 50:
		result += len(time)
	elif number == 60:
		result += len(time)
	elif number == 70:
		result += len(time)
	elif number == 80:
		result += len(time)
	elif number == 90:
		result += len(time)
	elif number == 100:
		result += len(time) - 1
	elif number > 20 and number < 100:
		result += len(time) - 1
	elif number > 100:
		i = str(number)[0]
		if number > int(i + '00') and number <= int(i + '20'):
			result += len(time) - 3
		elif number == int(i + '00'):
			result += len(time) - 1
		elif number == int(i + '30'):
			result +=  len(time) - 3
		elif number == int(i + '40'):
			result += len(time) - 3
		elif number == int(i + '50'):
			result += len(time) - 3
		elif number == int(i + '60'):
			result += len(time) - 3
		elif number == int(i + '70'):
			result += len(time) - 3
		elif number == int(i + '80'):
			result += len(time) - 3
		elif number == int(i + '90'):
			result += len(time) - 3
		else:
			result += len(time) - 4

print(result+11)

# brainless solving

