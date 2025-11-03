#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.



alphabet = 'abcdefghijklmnopqrstuvwxyz'
ciphertext = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

print("Расшифровка для всех сдвигов (0–25):\n")
for shift in range(26):
    result = ''
    for char in ciphertext:
        if char.lower() in alphabet:
            idx = alphabet.index(char.lower())
            new_idx = (idx - shift) % 26
            new_char = alphabet[new_idx]
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    print(f"Сдвиг {shift:2}: {result}")
