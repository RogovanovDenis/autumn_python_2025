# todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.

prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "18.99", "N/A", "¥5000"]
rates = {'USD': 95, 'EUR': 100, 'JPY': 0.6}

result = []

for item in prices:
    if not any(c.isdigit() for c in item):
        continue
    if 'USD' in item or '$' in item:
        value = float(item.replace('USD', '').replace('$', ''))
        value *= rates['USD']  # переводим в рубли
    elif 'EUR' in item or '€' in item:
        value = float(item.replace('EUR', '').replace('€', ''))
        value *= rates['EUR']
    elif '¥' in item:
        value = float(item.replace('¥', ''))
        value *= rates['JPY']
    elif '₽' in item:
        value = float(item.replace('₽', ''))  # уже в рублях
    else:
        value = float(item)

    result.append(value)

print(result)
