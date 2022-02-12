class InconsistentDataError (Exception):
    pass

print ('Значения катетов вводите через пробел')
leg_a = str.split (input ('Введите первые катеты a: '))
leg_b = str.split (input ('Введите вторые катеты b: '))

if len(leg_a) != len(leg_b):
    raise InconsistentDataError ('Массивы с катетами имеют разную длину')

for index, (a ,b) in enumerate (zip (leg_a, leg_b), 1):
    try:
        a, b = float (a), float (b)
        c = (a ** 2 + b ** 2) ** 0.5
        S = (a * b) / 2
    except ValueError:
        print ('NonNumberError: проверьте введенные данные')
        break
    print (f'Треугольник {index} с катетами {a} и {b} имеет площадь {S} и гипотенузу {c}')