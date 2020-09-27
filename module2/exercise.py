a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

age_min = 18

viewer1 = {'name': 'Иван', 'age': 34}
viewer2 = {'name': 'Марья', 'age': 16}

if viewer1['age'] >= age_min:
    print(f"Зритель {viewer1['name']} может смотреть фильм")
else:
    print(f"Зритель {viewer1['name']} не может смотреть фильм")

if viewer2['age'] >= age_min:
    print(f"Зритель {viewer2['name']} может смотреть фильм")
else:
    print(f"Зритель {viewer2['name']} не может смотреть фильм")