def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip() #прибирає все зайве з початку і кінця рядка
                if not line: #Пропускаємо порожні рядки
                    continue
                parts = line.split(",") #ділить рядок на список частин
                if len(parts) != 3:
                    print (f"Пропущено некоректний рядок: {line}")
                    continue
                cat_id, name, age = parts
                cats.append({"id": cat_id,"name": name, "age": age})
        return cats
    except FileNotFoundError:  #файл не існує
        print(f"Помилка: файл '{path}' не знайдено.")
        return []
    except Exception as e:   #усі інші помилки
        print(f"Сталася помилка: {e}")
        return []
    
cats_info = get_cats_info("cat/cats_file.txt")
print(cats_info)
