import math as m
'''
Тема: Биномиальный коэффициент
Было по теории вероятностей.
В таблцие 2х2 до достижения цели нужно
4 хода, при этом можно сделать 2 хода вниз
и 2 хода вправо.
Поэтому в 40х40 ...
'''

# Всего ходов до достижения цели 40
x = m.factorial(40)
# Всего 20 вниз и 20 вверх(возомжно сделать ходов)
# Сколькими способами можно выбрать 20 штук и 40 ?
y = m.factorial(20)
result = x/(m.factorial(40-20)*y)
print(result)