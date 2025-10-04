#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
A = int(input())
B = int(input())
C = int(input())
AC = max(A, C) - min(A, C)
BC = max(B, C) - min(B, C)
print(f'Длина отрезка AC: {AC}, длина отрезка BC: {BC}, сумма AB + BC: {AC + BC}')