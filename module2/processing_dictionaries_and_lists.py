user1 = {'name': 'Иван', 'age': 20, 'account': {'login': 'ivan', 'password': 'q1'}} # данные пользователей
user2 = {'name': 'Петр', 'age': 25, 'account': {'login': 'petr', 'password': 'q2'}}
user3 = {'name': 'Ольга', 'age': 18, 'account': {'login': 'olga', 'password': 'q3'}}
user4 = {'name': 'Анна', 'age': 27, 'account': {'login': 'anna', 'password': 'q4'}}

user_list = [user1, user2, user3, user4] # список пользователей

key = input("Введите ключ (name или account): ") # ключ для вывода данных по именам или аккаунтам из словарей user

try: # вывод данных по ключу
    print(f'значение ключа {key} для юзера 1 = {user1[key.lower()]}') # .lower() замена ПРОПИСНЫХ букв на строчные, есть буквы введённого ключас будут с разным регистром
    print(f'значение ключа {key} для юзера 2 = {user2[key.lower()]}')
    print(f'значение ключа {key} для юзера 3 = {user3[key.lower()]}')
    print(f'значение ключа {key} для юзера 4 = {user4[key.lower()]}')

except KeyError: # если введён некорректный ключ
    print ("Введенный ключ не найден")

# блок вывода данных из словарей user и account
sequence_number = int(input('Введите порядковый номер: ')) # порядковый номер для вывода данных из словарей user и account

print(f'Данные по юзеру №{sequence_number}:')
print(f"имя: {user_list[int(sequence_number)-1]['name']}")
print(f"возраст: {user_list[int(sequence_number)-1]['age']}")
print(f"логин: {user_list[int(sequence_number)-1]['account']['login']}")
print(f"пароль: {user_list[int(sequence_number)-1]['account']['password']}")

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