# 1ое решение.
numbers = []
counter = 0

while True:
	counter += 1
	if counter % 3 == 0:
		numbers.append(counter)
	if counter % 5 == 0:
		numbers.append(counter)
	if counter == 999:
		break

print(numbers)

result = 0
for number in numbers:
	result += number

print(result)

# Второе решение.
result = [x for x in range(1,1000) if x%3==0 or x%5==0]
print(result)
print(sum(result))

	




