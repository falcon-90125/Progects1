password = input("Введите пароль: ")

try:
    result = 1/len(password) # условие для исключения пустого пароля
    result = int(password) # условие для исключения пароля "только цифры"
    print("Ваш пароль состоит только из цифр")

except ZeroDivisionError:
    print("Вы ввели пустой пароль")
    
except ValueError: # если int в условии не смог преобразовать пароль значит есть буквы
    print("Требования к паролю соблюдены")
