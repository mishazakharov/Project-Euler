'''
for n in range(1,11):
	number%n == 0
'''
'''
result = 0
for number in range(200000000,299999000):
	i = 1
	while i != 19:
		i += 1
		if number%i == 0:
			if i == 20:
				result = number
			continue
		else:
			break


print(result)
'''
i = 10 
r = [x for x in range(3,20) if x != 10]
c = False
while c == False:
	for delitel in r:
		if i%delitel == 0:
			c = True
			continue
		else:
			c = False
			break
	i += 10




print(r)
print(i-10)