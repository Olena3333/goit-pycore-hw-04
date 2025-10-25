import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)  # щоб кольори не "тягнулися" далі

def print_tree(directory, indent=""):
    """Рекурсивно виводить структуру папки."""
    for item in directory.iterdir():
        if item.is_dir():
            # Папки сині
            print(f"{indent}{Fore.BLUE}{item.name}/")
            print_tree(item, indent + "    ")
        else:
            # Файли зелені
            print(f"{indent}{Fore.GREEN}{item.name}")

def main():
    # Отримуємо шлях із аргументів
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до папки.")
        return

    path = Path(sys.argv[1])

    # Перевірка на існування
    if not path.exists():
        print("Помилка: такий шлях не існує.")
        return
    if not path.is_dir():
        print("Помилка: шлях не веде до директорії.")
        return

    print(f"{Style.BRIGHT}Структура директорії: {path}\n")
    print_tree(path)

if __name__ == "__main__":
    main()

    #python print_tree.py "/Users/helensolonikova/Desktop/Python/goit-pycore-hw-04"
