password = input ("Введите пароль: ")
try:
    password.isnumeric()
    print("Требования к паролю соблюдены")
except:
    print("Ваш пароль состоит только из цифр")
