import sys
from pathlib import Path
from colorama import Fore, Style


def show_directory(path, level=0):
    for item in path.iterdir():
        indent = "    " * level

        if item.is_dir():
            print(f"{indent}{Fore.BLUE}📁 {item.name}{Style.RESET_ALL}")
            show_directory(item, level + 1)

        elif item.is_file():
            print(f"{indent}{Fore.GREEN}📄 {item.name}{Style.RESET_ALL}")


if len(sys.argv) < 2:
    print("Будь ласка, вкажіть шлях до директорії.")
else:
    path = Path(sys.argv[1])

    if not path.exists():
        print(f"Помилка: шлях '{path}' не існує.")
    elif not path.is_dir():
        print(f"Помилка: '{path}' не є директорією.")
    else:
        try:
            print(f"{Fore.BLUE}📁 {path.name}{Style.RESET_ALL}")
            show_directory(path, 1)
        except OSError as error:
            print(f"Помилка під час читання директорії: {error}")