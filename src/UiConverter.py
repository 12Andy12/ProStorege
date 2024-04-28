import re
import os


def convert_ui_to_py():
    files = os.listdir("ui")
    for file in files:
        if re.match(r'.*\.ui', file):
            print(f'Файл {file} обнаружен')
            file_py = file[:-2] + "py"
            command = f"pyside6-uic ui/{file} > src/forms/{file_py}"
            os.popen(command)
            print(f'Файл {file_py} создан')