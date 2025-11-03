#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = input('Введите числа через пробел: ')
number_strings = text.split()
result = ''

for num_str in number_strings:
    if num_str.isdigit():
        num = int(num_str)
        if num == 0:
            result += ' '
        elif 1 <= num <= 26:
            letter = alphabet[num - 1]
            result += letter
    else:
        result += num_str
print(result)
