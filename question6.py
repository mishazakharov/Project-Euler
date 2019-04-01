sum_squares = []
square_sum = []

for number in range(1,101):
	sum_squares.append(number**2)
	square_sum.append(number)

a = sum(sum_squares)

b = sum(square_sum)**2

answer = b - a
print(answer)