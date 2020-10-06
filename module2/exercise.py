student1 = {'name': 'Иван', 'cities': ['Москва', 'Лондон']}
student2 = {'name': 'Мария', 'cities': ['Париж', 'Нью Йорк']}
student3 = {'name': 'Петр', 'cities': ['Пекин', 'Токио']}

students = [student1, student2, student3]

city = 'Париж'

name = ''
iterations = 0
for student in students:
    iterations += 1
    if city in student['cities']:
        name = student['name']
print(f'Количество итераций: {iterations}')

name = ''
iterations = 0
for student in students:
    iterations += 1
    if city in student['cities']:
        name = student['name']
    if name:
        break # прерываем цикл если нашли студента
print(f'Количество итераций: {iterations}')
