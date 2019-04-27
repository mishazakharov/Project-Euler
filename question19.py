'''
Допустим 7ое числа января 1900 года - это воскресенье, тогда:
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
needed_days = []
# i - переменная, хранящая информацию о дне недели:
i = 1

for year in range(beginning_year,2000):
	for month in casual_year.keys():
		# Если год - високосный
		if year%4 == 0:
			# Для февраля добавляется один день
			# это единственный способ, до которого я додумался сейчас!
			if month == 'February':
				for day in range(casual_year[month]+1):
					if day == 0 and i == 7:
						needed_days.append(day)
					i += 1
					if i == 8:
						i = 1
				continue
		for day in range(casual_year[month]):
			# Добавляет только воскресенья, с которых начинается месяц....
			if day == 0 and i == 7:
				needed_days.append(day)
			# Обновление дней недели
			i += 1
			# С понедельника по воскресенье
			if i == 8:
				i = 1

print(len(needed_days))