import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)  # щоб кольори не "тягнулися" далі


# Функція для рекурсивного виведення структури папки
def print_tree(path: Path, prefix=""):
    if not path.exists() or not path.is_dir():
        print(f"{Fore.RED}Помилка: {path} не існує або не є папкою{Style.RESET_ALL}")
        return

    items = sorted(list(path.iterdir()), key=lambda x: (x.is_file(), x.name.lower()))
    for i, item in enumerate(items):
        connector = "┗" if i == len(items)-1 else "┣"

        if item.is_dir():
            print(f"{prefix}{connector} 📂{Fore.GREEN}{item.name}{Style.RESET_ALL}")
            # Рекурсивно виводимо підпапки
            new_prefix = prefix + ("   " if i == len(items)-1 else "┃  ")
            print_tree(item, new_prefix)
        else:
            print(f"{prefix}{connector} 📜{Fore.BLUE}{item.name}{Style.RESET_ALL}")

# Основна частина скрипта
def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Будь ласка, вкажіть шлях до папки{Style.RESET_ALL}")
        return

    path = Path(sys.argv[1])
    print_tree(path)

if __name__ == "__main__":
    main()