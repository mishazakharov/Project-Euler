fibo = [1,2]

for n in range(1,1000):
	next_number = (fibo[-1] + fibo[-2])
	fibo.append(next_number)

result = [x for x in fibo if x%2 == 0 and x<4000000]

print(sum(result))
