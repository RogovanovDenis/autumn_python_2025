#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

file = open("inverted_sort.txt", "a+")
file.write("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.\n""")
# file.close()
file = open("inverted_sort.txt", "a+")
new_text = file.readlines()
rev_text = []
#print(new_text)
for line in new_text:
    rev_text.append(line)
for rev in rev_text[::-1]:
    file.write(rev)
file.close()

#Содержимое файла inverted_sort.txt
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.

# Результат
#Complex is better than complicated.
#Simple is better than complex.
#Explicit is better than implicit.
#Beautiful is better than ugly.