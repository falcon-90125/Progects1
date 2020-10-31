#++++++++++++++++++++++++++++
#Подсчет количества элементов
#++++++++++++++++++++++++++++

# def quantity(object_list):
#     result = 0
#     for i in object_list:
#         result += 1
#     return result

# item_list = ['Яблоко', 'Апельсин', 'Банан', 'Автомобиль', 'Телефон', 'Груша']

# print(f'Количество элементов = {quantity(item_list)}')
# #Мой вариант
# print(f'Количество элементов = {len(item_list)} (Мой вариант)')


# #Функцию напрямую можно использовать в условиях. Например, выведем количество элементов, только если оно больше 10:
# if quantity(item_list) > 10:
#     print('Количество элементов в списке больше 10')

#++++++++++++++++++++++++
# Поиск в списке словарей
#++++++++++++++++++++++++

def quantity(object_list, is_fruit=None):
    result = 0
    for i in object_list:
        if is_fruit is None or i['is_fruit'] == is_fruit:
            result += 1
    return result


item_list = [{'title': 'Яблоко', 'is_fruit': True},
             {'title': 'Апельсин', 'is_fruit': True},
             {'title': 'Банан', 'is_fruit': True},
             {'title': 'Автомобиль', 'is_fruit': False},
             {'title': 'Телефон', 'is_fruit': False},
             {'title': 'Груша', 'is_fruit': True}, ]

print(f'Количество фруктов = {quantity(item_list, is_fruit=True)}')
print(f'Количество не фруктов = {quantity(item_list, is_fruit=False)}')
print(f'Количество элементов всего = {quantity(item_list)}')




# https://pumpskill.ru/courses/bazovyy-kurs-python/lessons/osnovy-strukturnogo-programmirovaniya/poisk-vo-vlozhennykh-kollekciyakh-s-pomoshyu-funkciy/
