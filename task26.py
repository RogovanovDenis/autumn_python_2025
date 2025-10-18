#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

#Формат вывода:
#Количество букв a - 13
#Количество букв o - 12
#Количество букв e - 11
#.....................

f = open("Pushkin.txt", "r", encoding="utf-8")
lines = f.readlines()

a = [i for line in lines for i in line if i == 'а' or i =='А']
o = [i for line in lines for i in line if i == 'о' or i =='О']
e = [i for line in lines for i in line if i == 'е' or i =='Е']
u = [i for line in lines for i in line if i == 'и' or i =='И']
y = [i for line in lines for i in line if i == 'у' or i =='У']
b = [i for line in lines for i in line if i == 'э' or i =='Э']
c = [i for line in lines for i in line if i == 'ы']
n = [i for line in lines for i in line if i == 'ё' or i =='Ё']
p = [i for line in lines for i in line if i == 'ю' or i =='Ю']
q = [i for line in lines for i in line if i == 'я' or i =='Я']
print(f'''
Количество букв a - {len(a)}
Количество букв o - {len(o)}
Количество букв e - {len(e)}
Количество букв и - {len(u)}
Количество букв у - {len(y)}
Количество букв э - {len(b)}
Количество букв ы - {len(c)}
Количество букв ё - {len(n)}
Количество букв ю - {len(p)}
Количество букв я - {len(q)}''')
f.close()
