time = 0
for n in range(100,1000):
	for i in range(100,1000):
		answer = str(n*i)
		if answer[0] == answer[-1] and answer[1] == answer[-2] and answer[2] == answer[-3]:
			result = int(answer)
			if time < result:
				time = result
print(time)