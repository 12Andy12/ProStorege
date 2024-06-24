import re
import os

# python src/UiConverter.py


def convert_ui_to_py():
    os.popen("poetry shell")
    print("start convert")
    files = os.listdir("ui")
    for file in files:
        if re.match(r".*\.ui", file):
            print(f"Файл {file} обнаружен")
            file_py = file[:-2] + "py"
            command = f"pyside6-uic ui/{file} > src/forms/{file_py}"
            os.popen(command)
            print(f"Файл {file_py} создан")
    os.popen("exit")


if __name__ == "__main__":
    convert_ui_to_py()
