account1 = {'login': 'ivan', 'password': 'q1'} # данные аккаунтов
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': 'account1'} # данные пользователей
user2 = {'name': 'Петр', 'age': 25, 'account': 'account2'}
user3 = {'name': 'Ольга', 'age': 18, 'account': 'account3'}
user4 = {'name': 'Анна', 'age': 27, 'account': 'account4'}

user_list = [user1, user2, user3, user4] # список пользователей

key = input("Введите ключ (name или account): ") # ключ для вывода данных по именам или аккаунтам из словарей user
user_key = key.lower() # замена ПРОПИСНЫХ букв на строчные

try: # вывод данных по ключу
    print(f'значение ключа {key} для юзера 1 = {user1[user_key]}')
    print(f'значение ключа {key} для юзера 2 = {user2[user_key]}')
    print(f'значение ключа {key} для юзера 3 = {user3[user_key]}')
    print(f'значение ключа {key} для юзера 4 = {user4[user_key]}')

except KeyError: # если введён некорректный ключ
    print ("Введенный ключ не найден")

# блок вывода данных из словарей user и account
sequence_number = int(input('Введите порядковый номер: ')) # порядковый номер для вывода данных из словарей user и account

if sequence_number > 4: # для исключения отсутствующих номеров, нужны только от 1 до 4
    print('Пользователь с указанным номером не найден')
elif sequence_number < 1: # для исключения отсутствующих номеров, нужны только от 1 до 4
    print('Пользователь с указанным номером не найден')
elif sequence_number == 1: # уловие для вывода данных по номеру юзера
    print (f"имя: {user1['name']}")
    print (f"возраст: {user1['age']}")
    print (f"логин: {account1['login']}")
    print (f"пароль: {account1['password']}")
elif sequence_number == 2: # уловие для вывода данных по номеру юзера
    print ('Данные по юзеру №' + str(sequence_number) + ':')
    print (f"имя: {user2['name']}")
    print (f"возраст: {user2['age']}")
    print (f"логин: {account2['login']}")
    print (f"пароль: {account2['password']}")
elif sequence_number == 3: # уловие для вывода данных по номеру юзера
    print ('Данные по юзеру №' + str(sequence_number) + ':')
    print (f"имя: {user3['name']}")
    print (f"возраст: {user3['age']}")
    print (f"логин: {account3['login']}")
    print (f"пароль: {account3['password']}")
else: # уловие для вывода данных по номеру юзера
    print ('Данные по юзеру №' + str(sequence_number) + ':')
    print (f"имя: {user4['name']}")
    print (f"возраст: {user4['age']}")
    print (f"логин: {account4['login']}")
    print (f"пароль: {account4['password']}")

# блок переноса пользователя в конец списка
user_number = int(input('Введите номер пользователя, которого нужно переместить в конец: '))
user_number_adapted = int(user_number) - 1 # порядковый номер адаптированный под user_list

print('Список до изменения:')
print(user_list) # вывод списка до переноса

user_list.append(user_list[user_number_adapted]) # добавление пользователя в конец списка
user_list.remove(user_list[user_number_adapted]) # удаление пользователя из исходного списка

print('Список после изменения:')
print(user_list) # вывод списка после переноса

middle_age = (user1['age'] + user2['age'] + user3['age'] + user4['age'])/4 # вычесление среднего возраста пользователей
print("Cредний возраст всех юзеров: " + str(middle_age))