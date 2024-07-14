def total_salary(path: str) -> list or None:
    salaries = []
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                # ігноруємо порожні рядки
                if len(line.strip()) == 0:
                    continue

                _, salary = line.strip().split(',')

                if not salary.isdigit():
                    raise ValueError(f'Файл містить невалідні дані. [Рядок "{line.strip()}"]')

                salaries.append(int(salary))

            return [sum(salaries), sum(salaries) / len(salaries)]
    except FileNotFoundError:
        print(f'Файл не знайдено [Шлях "{path}"]')
    except ValueError as error:
        print(error)
    except ZeroDivisionError:
        print(f'Файл порожній [Шлях "{path}"]')

    return None



if __name__ == '__main__':
    # correct
    total, average = total_salary('./salaries.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.0f}")

    # file not found
    total_salary('./not_found_salaries.txt')

    # invalid data in file
    total_salary('./salaries_invalid.txt')

    # empty file
    total_salary('./salaries_empty.txt')
