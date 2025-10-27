def total_salary(path):
    try:  
        with open(path, "r", encoding="utf-8") as file: 
            salaries = []
            for line in file:  
                name, salary = line.strip().split(",") 
                salaries.append(int(salary)) 
            total = sum(salaries) 
            average = total / len(salaries) 
            return total, average
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("salary/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
