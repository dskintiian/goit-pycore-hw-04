def get_cats_info(path: str) -> list or None:
    cats = []
    try:
        with open(path) as file:
            for line in file:
                # ігноруємо порожні рядки
                if len(line.strip()) == 0:
                    continue

                id, name, age = line.strip().split(',')
                cats.append({'id': id, 'name': name, 'age': age})

        return cats
    except FileNotFoundError:
        print(f'Файл не знайдено [Шлях "{path}"]')

        return None

if __name__ == '__main__':
    #correct
    cats_info = get_cats_info("./cats.txt")
    print(cats_info)

    # file not found
    cats_info = get_cats_info("./no_cats.txt")
