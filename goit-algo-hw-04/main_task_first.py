def total_salary(path):
    employees = []
    try:
        with open(path, 'r+', encoding='utf-8') as file:
            data = file.readlines()

        for empl in data:
            parts = empl.strip().split(',')
            employees.append({
                'employee': parts[0],
                'salary': int(parts[1])
            })

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено")
        return 0, 0  # возвращаем кортеж с нулями

    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return 0, 0

    if not employees:
        return 0, 0

    salary_total = sum(empl['salary'] for empl in employees)
    salary_average = int(salary_total / len(employees))

    return salary_total, salary_average


if __name__ == '__main__':
    total, average = total_salary('salaryY.txt')

    print(f"Загальна сума заробітної плати: {total}, "
          f"Середня заробітна плата: {average}")
