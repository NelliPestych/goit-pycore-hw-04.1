def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                salary = int(salary)

                total += salary
                count += 1

        if count == 0:
            return 0, 0

        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
    except ValueError:
        print("Помилка: файл містить некоректні дані.")
    except OSError as error:
        print(f"Помилка читання файлу: {error}")

    return 0, 0

total, average = total_salary("data/salary_file.txt")

print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")