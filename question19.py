'''
Допустим 7ое числа января 1900 года - это воскресенье, тогда:

i= 1 - понедельник
i= 2 - вторник
i= 7 - воскресенье
'''

casual_year = {
			'January':31,
			'February':28,
			'March':31,
			'April':30,
			'May':31,
			'June':30,
			'July':31,
			'August':31,
			'September':30,
			'October':31,
			'November':30,
			'December':31,
			}

beginning_year = 1901

for year in range(beginning_year,2001):
	# Если год - високосный
	if year%4 == 0:
		for month in casual_year.keys():
			# Для февраля добавляется один день
			# это единственный способ, до которого я додумался сейчас!
			if month == 'February':
				for day in range(casual_year[month]+1):
					pass
				continue
			for day in range(casual_year[month]):
				pass
	# Если год обычный
	else:
		for month in casual_year.keys():
			# i - переменная, хранящая информацию о дне недели:
			i = 1
			for day in range(casual_year[month]):
				if day%(8-i) == 0:
					print(day)




