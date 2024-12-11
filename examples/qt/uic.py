import os
from PyQt6.uic import compileUi

# Получаем текущую папку
# os.getcwd() используется для получения текущей рабочей директории, откуда запускается скрипт
current_dir = os.getcwd()

# Проходимся по всем файлам в папке
# os.listdir() возвращает список всех файлов и директорий в указанной папке
for file_name in os.listdir(current_dir):
    # Фильтруем только файлы с расширением .ui для обработки
    if file_name.endswith('.ui'):
        # Формируем имя выходного файла
        py_file_name = file_name.replace('.ui', '.py')
        
        try:
            with open(py_file_name, 'w', encoding='utf-8') as output_file:
                # compileUi используется для преобразования .ui файла в .py файл
                compileUi(file_name, output_file)
            # Выводим сообщение для информирования об успешной конвертации
            print(f"Успешно скомпилирован: {file_name} -> {py_file_name}")
        except Exception as e:
            print(f"Ошибка при обработке {file_name}: {e}")
