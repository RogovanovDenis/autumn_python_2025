#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
#Пример:
import random
mass = [1,2,17,54,30,89,2,1,6,2]

x = random.randint(1,100)

mass_index_var =[]
#Значения индексов числа в списке
for i in range(len(mass)):
     if mass[i] == x:
         mass_index_var.append(i)
#print(mass_index_var)
check =[]

#Нахождение расстояний между индексами (по модулю)
for val_check in range(len(mass_index_var)):
    new = mass_index_var[val_check] - mass_index_var[val_check-1]
    check.append(new)
    positive_numbers = [abs(num) for num in check]
if len(check) == 1 or len(check) == 0:
    print("Нет минимально расстояния")
    exit()
print(f'Для числа {x} минимальное расстояние: {min(positive_numbers)}')

#Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
#Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
#Для числа 17 нет минимального растояния т.к элемент в массиве один.
