persons = [
    {
        'name': 'Mik',
        'age': 36,
        'gender': 'male',
    }, {
        'name': 'Valera',
        'age': 12,
        'gender': 'male',
    }, {
        'name': 'Joan',
        'age': 18,
        'gender': 'female',
    }, {
        'name': 'Maik',
        'age': 47,
        'gender': 'male',
    }, {
        'name': 'Amanda',
        'age': 32,
        'gender': 'female',
    }, {
        'name': 'Anastasia',
        'age': 19,
        'gender': 'female',
    }, {
        'name': 'Valera',
        'age': 45,
        'gender': 'male',
    }, {
        'name': 'Ariel',
        'age': 16,
        'gender': 'female',
    }, {
        'name': 'Veronica',
        'age': 13,
        'gender': 'female',
    }, {
        'name': 'Valera',
        'age': 42,
        'gender': 'male',
    }, {
        'name': 'Jessie',
        'age': 19,
        'gender': 'female',
    }, {
        'name': 'Jessie',
        'age': 19,
        'gender': 'female',
    }, {
        'name': 'Tracy',
        'age': 24,
        'gender': 'female',
    }, {
        'name': 'Mik',
        'age': 29,
        'gender': 'another',
    }, {
        'name': 'Jessie',
        'age': 33,
        'gender': 'female',
    }, {
        'name': 'Valera',
        'age': 15,
        'gender': 'male',
    }, {
        'name': 'Tracy',
        'age': 23,
        'gender': 'female',
    }, {
        'name': 'Maria',
        'age': 29,
        'gender': 'female',
    }, {
        'name': 'Pamela',
        'age': 91,
        'gender': 'female',
    }, {
        'name': 'Bobby',
        'age': 28,
        'gender': 'male',
    }, {
        'name': 'Tracy',
        'age': 24,
        'gender': 'female',
    }, {
        'name': 'Tracy',
        'age': 17,
        'gender': 'female',
    }, {
        'name': 'Gregory',
        'age': 17,
        'gender': 'male',
    }
]
number = len(persons)
print (f'количество всех людей: {number}')

gender = {}
for index in range(len(persons)):
    if persons [index]['gender']  not in gender:
        gender |= {persons [index]['gender']: 1}
    else:
        gender [persons [index]['gender']] += 1
print (f"количество мужчин: {gender['male']}, женщин: {gender['female']}, не определились: {gender['another']}")

adult, minor = 0, 0 
for index in range(len(persons)):
    if persons [index]['age'] >= 18:                                    
        adult +=1 
    else: 
        minor +=1 
print (f'совершеннолетних: {adult}, несовершеннолетних: {minor}')
# adult = 0  
# for index in range(len(persons)):
#     if persons [index]['age'] >= 18:
#         adult +=1 
#  print (f'совершеннолетних: {adult}, несовершеннолетних: {len(persons)-adult}')

name = [persons [index]['name'] for index in range (len(persons))]
print (f'список всех имен: {name}')

age = sorted(set( [persons [index]['age'] for index in range (len(persons))] ))
print (f'список всех возрастов: {age}')

from collections import Counter
counter_name = Counter (name)
print (f"самые популярные имена: {counter_name.most_common(3)}")

print ('Имена которые начинаются на букву "M":', end = ' ')
for index in range(len(persons)):
    if persons[index]['gender'] == 'male' and persons[index]['age'] >= 35:
            name_letters = list(persons[index]['name'])
            if name_letters[0] == 'M':
                print (persons[index]['name'], end = ' ')
