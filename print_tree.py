import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)  # щоб кольори не "тягнулися" далі

def print_tree(directory, indent=""):
    for item in directory.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/") # Папки сині
            print_tree(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")  # Файли зелені

if len(sys.argv) < 2:
    print("Будь ласка, вкажіть шлях до папки.")
else:
    path = Path(sys.argv[1])

    if not path.exists():
        print("Помилка: такий шлях не існує.")
    elif not path.is_dir():
        print("Помилка: шлях не веде до директорії.")
    else:
        print(f"{Style.BRIGHT}Структура директорії: {path}\n")
        print_tree(path)

#python3 -m venv .venv
#source .venv/bin/activate
#pip install colorama
#pip list
#pip freeze > requirements.txt
#pip install -r requirements.txt
#python print_tree.py "/Users/helensolonikova/Desktop/Python/goit-pycore-hw-04"
