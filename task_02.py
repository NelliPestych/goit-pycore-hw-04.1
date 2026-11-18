
def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return []

    except (ValueError, UnicodeError):
        print("Помилка: файл містить некоректні дані.")
        return []

    except OSError as error:
        print(f"Помилка читання файлу: {error}")
        return []

    return cats


cats_info = get_cats_info("data/cats_file.txt")
print(cats_info)
