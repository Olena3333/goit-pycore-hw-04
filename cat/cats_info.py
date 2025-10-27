def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip() 
                if not line: 
                    continue
                parts = line.split(",") 
                if len(parts) != 3:
                    print (f"Пропущено некоректний рядок: {line}")
                    continue
                cat_id, name, age = parts
                cats.append({"id": cat_id,"name": name, "age": age})
        return cats
    except FileNotFoundError:  
        print(f"Помилка: файл '{path}' не знайдено.")
        return []
    except Exception as e:   
        print(f"Сталася помилка: {e}")
        return []
    
cats_info = get_cats_info("cat/cats_file.txt")
print(cats_info)
