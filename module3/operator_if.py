# Турист Мария возраст 22. Посетил город Париж

cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35}, {'name': 'Мария', 'age': 22}, {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[0]}, {'user': users[1], 'city': cities[1]}, {'user': users[2], 'city': cities[2]}]

city = input('Введите город: ')

user0 = users[0]
user1 = users[1]
user2 = users[2]

if city == (cities[0]):
    print (f"Турист {user0['name']} возраст {user0['age']}.")
else:
    if city == (cities[1]):
        print (f"Турист {user1['name']} возраст {user1['age']}.")
    else:
        if city == (cities[2]):
            print (f"Турист {user2['name']} возраст {user2['age']}.")
        else:
            print ('Нет такого города')
