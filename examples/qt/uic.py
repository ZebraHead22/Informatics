import os
from PyQt6.uic import compileUi

# Получаем текущую папку
current_dir = os.getcwd()

# Проходимся по всем файлам в папке
for file_name in os.listdir(current_dir):
    if file_name.endswith('.ui'):
        # Формируем имя выходного файла
        py_file_name = file_name.replace('.ui', '.py')
        
        try:
            with open(py_file_name, 'w', encoding='utf-8') as output_file:
                compileUi(file_name, output_file)
            print(f"Успешно скомпилирован: {file_name} -> {py_file_name}")
        except Exception as e:
            print(f"Ошибка при обработке {file_name}: {e}")