cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35}, {'name': 'Мария', 'age': 22}, {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[0]}, {'user': users[1], 'city': cities[1]}, {'user': users[2], 'city': cities[2]}]

city = input('Введите город: ')

# Моё решение
if city.lower().title() == (cities[0]): # сравнение введёного города со списком cities
    print (f"Турист {users[0]['name']} возраст {users[0]['age']}. Посетил город {city.lower().title()}") # вывод имени, возраста туриста и города посещения, соотв. введённому
else:
    if city.lower().title() == (cities[1]): # сравнение введёного города со списком cities
        print (f"Турист {users[1]['name']} возраст {users[1]['age']}. Посетил город {city.lower().title()}") # вывод имени, возраста туриста и города посещения, соотв. введённому
    else:
        if city.lower().title() == (cities[2]): # сравнение введёного города со списком cities
            print (f"Турист {users[2]['name']} возраст {users[2]['age']}. Посетил город {city.lower().title()}") # вывод имени, возраста туриста и города посещения, соотв. введённому
        else:
            print ('Такой город ни кто неs посещал') # если введён город не из списка

# Решил: sleovochkina@gmail.com
# if city in cities:
#     for tourist in tourists:
#         if tourist['city'] == city:
#             print(f"Турист {tourist['user']['name']} возраст {tourist['user']['age']}. Посетил город {tourist['city']}")
# else:
#     print('Этот город еще никто не посещал')