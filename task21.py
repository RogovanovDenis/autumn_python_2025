#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

# Содержимое файла config_default.txt
# Конфигурация приложения.
# app_name    = ?
# version     = ?
# debug       = ?
#
# # Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?
#
# # Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?
#
# # Пути
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?


# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

# В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True
#
# # Настройки базы данных
# db_host     =  5432
# .....

with open('config_default.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
output_lines = []
for line in lines:
    if '=' in line and '?' in line:
        param_name = line.split('=')[0].strip()
        if param_name in config_values:
            value = config_values[param_name]
            if isinstance(value, str):
                new_line = f"{param_name} = \"{value}\"\n"
            else:
                new_line = f"{param_name} = {value}\n"
            output_lines.append(new_line)
        else:
            # Если параметра нет в словаре — оставляем как есть
            output_lines.append(line)
    else:
        # Строки без "=" или "?" оставляем без изменений (комментарии и пр.)
        output_lines.append(line)

with open('config.txt', 'w', encoding='utf-8') as file:
    file.writelines(output_lines)

print("Файл config.txt успешно создан!")