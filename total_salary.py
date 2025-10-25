def total_salary(path):
    try:   #якщо файл відсутній або у ньому помилка
        with open(path, "r", encoding="utf-8") as file: #Відкриваємо файл для читання
            salaries = []
            for line in file:  #читає файл пострічково
                name, salary = line.strip().split(",") #strip() — прибирає пробіли, split(",") — ділить рядок за комою
                salaries.append(int(salary)) #додаємо зарплату до списку, але перетворюємо її у число
            total = sum(salaries) #загальна сума зарплат
            average = total / len(salaries) #середня зарплату
            return total, average
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

    

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
