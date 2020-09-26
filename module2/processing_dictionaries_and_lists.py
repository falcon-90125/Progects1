account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': 'account1'}
user2 = {'name': 'Петр', 'age': 25, 'account': 'account2'}
user3 = {'name': 'Ольга', 'age': 18, 'account': 'account3'}
user4 = {'name': 'Анна', 'age': 27, 'account': 'account4'}

user_list = [user1, user2, user3, user4]

# key = input("Введите ключ (name или account): ")
# user_key = key.lower()

# try:
#     print(f'значение ключа {user_key} для юзера 1 = {user1[user_key]}')
#     print(f'значение ключа {user_key} для юзера 2 = {user2[user_key]}')
#     print(f'значение ключа {user_key} для юзера 3 = {user3[user_key]}')
#     print(f'значение ключа {user_key} для юзера 4 = {user4[user_key]}')

# except KeyError:
#     print ("Введенный ключ не найден")

# sequence_number = int(input('Введите порядковый номер: ')) #порядковый номер
# #sequence_number_adapted = int(sequence_number) - 1 #порядковый номер адаптированный под user_list - может не пригодится

# if sequence_number > 4:
#     print('Пользователь с указанным номером не найден')
# elif sequence_number < 1:
#     print('Пользователь с указанным номером не найден')
# elif sequence_number == 1:
#     print ('имя: Иван')
#     print ('возраст: 20')
#     print ('логин: ivan')
#     print ('пароль: q1')
# elif sequence_number == 2:
#     print ('Данные по юзеру №' + str(sequence_number) + ':')
#     print ('имя: Петр')
#     print ('возраст: 25')
#     print ('логин: petr')
#     print ('пароль: q2')
# elif sequence_number == 3:
#     print ('Данные по юзеру №' + str(sequence_number) + ':')
#     print ('имя: Ольга')
#     print ('возраст: 18')
#     print ('логин: olga')
#     print ('пароль: q3')
# else:
#     print ('Данные по юзеру №' + str(sequence_number) + ':')
#     print ('имя: Анна')
#     print ('возраст: 27')
#     print ('логин: anna')
#     print ('пароль: q4')

user_number = int(input('Введите номер пользователя, которого нужно переместить в конец: '))
user_number_adapted = int(user_number) - 1 # порядковый номер адаптированный под user_list
print('Список до изменения:')
print(user_list)
user_list.append(user_list[user_number_adapted])
user_list.remove(user_list[user_number_adapted])
print('Список после изменения:')
print(user_list)
