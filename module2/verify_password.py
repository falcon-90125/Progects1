password = input ("Введите пароль: ")
try:
    result = password.isalpha()
except:
    print("Ваш пароль состоит только из цифр")
print("Требования к паролю соблюдены")