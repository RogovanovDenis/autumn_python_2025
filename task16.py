# todo: База данных пользователя.
# Задан массив объектов пользователя

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
number = int(input('''Введите тип сортировки:
1. По возрасту
2. По первой букве
3. По группе\n'''))

match number:
    case 1:
        age = int(input('Введите возраст: '))
        age_ = [(user['login'], user['age'], user['group']) for user in users if age < user['age']]
        for n, a, g in age_:
            if 11 <= (a % 100) <= 14:
                suffix = 'лет'
            elif a % 10 == 1:
                suffix = 'год'
            elif 2 <= (a % 10) <= 4:
                suffix = 'года'
            else:
                suffix = 'лет'
            print(f'Пользователь: {n}, возраст: {a} {suffix}, группа: {g}')
    case 2:
        name = input('Введите первую букву имени: ')
        name_ = [[user['login'], user['age'], user['group']] for user in users if name == user['login'][0]]
        for n, a, g in name_:
            if 11 <= (a % 100) <= 14:
                suffix = 'лет'
            elif a % 10 == 1:
                suffix = 'год'
            elif 2 <= (a % 10) <= 4:
                suffix = 'года'
            else:
                suffix = 'лет'
            print(f'Пользователь: {n}, возраст: {a} {suffix}, группа: {g}')
    case 3:
        group = input('''Введите группу:
Подсказка: admin, guest, master\n''')
        group_ = [[user['login'], user['age'], user['group']] for user in users if user['group'] == group]
        for n, a, g in group_:
            if 11 <= (a % 100) <= 14:
                suffix = 'лет'
            elif a % 10 == 1:
                suffix = 'год'
            elif 2 <= (a % 10) <= 4:
                suffix = 'года'
            else:
                suffix = 'лет'
            print(f'Пользователь: {n}, возраст: {a} {suffix}, группа: {g}')

#Затем сообщение для ввода
# Ввидите критерии поиска: 16
#
# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"




