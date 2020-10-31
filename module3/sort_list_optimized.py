def sort_list(my_list, direction=None):
    """Сортировка списка my_list методом пузырька.
    :param my_list: список значений
    :param direction: (опциональный) направление сортировки. Возможные значения: 1, -1
    (Это многострочный комментарий - он пишется через тройные кавычки)
    """
    
    if direction:
            # Сначала мы проверяем передано ли вообще что-то в параметр direction: if direction и только в этом случае выполняем сортировку.
            # Если ничего не передается, то direction будет равен None, а если значение не заполнено, то if возвращает False.
        for i in range(len(my_list)):
            for j in range(i, len(my_list)):
                if (direction == -1 and my_list[i] > my_list[j]) or (direction == 1 and my_list[i] < my_list[j]):
                # Если direction == -1 и текущий элемент больше следующего
                # или direction == 1 и текущий элемент меньше следующего,
                # то меняем местами элементы.
                    temp = my_list[i]
                    my_list[i] = my_list[j]
                    my_list[j] = temp
    return my_list


list1 = [4, -2, 5, 3, -1 , 1, 0, 5, 2]
list2 = [5, 3, 2, 5, 6 , -1, 0, -5, 2]
list3 = [7, 2, 4, 1, -1 , 7, 3, -5, 0]
list4 = [2, -5, 6, 1, 0 , -1, -2, -3, 9]
list5 = [9, 0, 1, 2, 9 , 3, -1, 4, 2]


# у 3го параметра direction не задан, поэтому сортировки по нему не будет из-за "if direction (is not None)"
sort_list(list1, 1)
sort_list(list2, 1)
sort_list(list3)
sort_list(list4, -1)
sort_list(list5, -1)

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

# https://pumpskill.ru/courses/bazovyy-kurs-python/lessons/osnovy-strukturnogo-programmirovaniya/parametry-funkciy/