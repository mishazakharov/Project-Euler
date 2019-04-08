import inflect

result = 0
p = inflect.engine()
for number in range(1,101):
	time = p.number_to_words(number)
	if len(time) > 8:
		result += len(time) - 1
	else:
		result += len(time)


print(result)



