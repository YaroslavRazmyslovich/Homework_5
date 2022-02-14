class InconsistentDataError (Exception):
    pass

print ('Значения катетов вводите через пробел')
legs= str.split (input ('Введите катеты: '))
if len(legs) % 2:
    raise InconsistentDataError ('Один катет лишний, ну или одного не хватает')

# Простой переход к предыдущей задаче
print ('Первый вариант решения')
leg_a = legs[::2]
leg_b = legs[1::2]

for index, (a ,b) in enumerate (zip (leg_a, leg_b), 1):
    try:
        a, b = float (a), float (b)
        c = (a ** 2 + b ** 2) ** 0.5
        S = (a * b) / 2
    except ValueError:
        print (f'NonNumberError: проверьте введенные данные катетов {index} треугольника')
    else:
        print (f'Треугольник {index} с катетами {a} и {b} имеет площадь {S} и гипотенузу {c}')

# Вариант с while и счетчиком индекса
print ('Второй вариант решения')
i = 0
while i <= len(legs) - 1:
    try:
        a, b = float (legs[i]), float (legs[i+1])
        c = (a ** 2 + b ** 2) ** 0.5
        S = (a * b) / 2
    except ValueError:
        i += 2
        print (f'NonNumberError: проверьте введенные данные катетов {i//2} треугольника')
    else:
        i += 2
        print (f'Треугольник {i//2} с катетами {a} и {b} имеет площадь {S} и гипотенузу {c}')

# Вариант с циклом for
print ('Третий вариант решения')
for index in range (0, len(legs), 2):
    try:
        a, b = float (legs[index]), float (legs[index+1])
        c = (a ** 2 + b ** 2) ** 0.5
        S = (a * b) / 2
    except ValueError:
        print (f'NonNumberError: проверьте введенные данные катетов {index//2+1} треугольника')
    else:
        print (f'Треугольник {index//2+1} с катетами {a} и {b} имеет площадь {S} и гипотенузу {c}')
