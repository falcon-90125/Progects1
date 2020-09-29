cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35}, {'name': 'Мария', 'age': 22}, {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[0]}, {'user': users[1], 'city': cities[1]}, {'user': users[2], 'city': cities[2]}]

#city = input('Введите город: ')

# print (f"Турист {users['name']} возраст {users['age']}.")

#element1 = cities.index(city)
print(tourists)
# [{'user': {'name': 'Иван', 'age': 35}, 'city': 'Москва'}, {'user': {'name': 'Мария', 'age': 22}, 'city': 'Париж'}, {'user': {'name': 'Соня', 'age': 20}, 'city': 'Лондон'}]