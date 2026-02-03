def get_cats_info(path):
    cats_info_lst = []
    try:
        with open(path, 'r+', encoding='utf-8') as file:
            data = file.readlines()

        for cat in data:
            cat_data = cat.strip().split(',')
            id = cat_data[0]
            name = cat_data[1]
            age = cat_data[2]

            cats_info_lst.append({
                'id': id,
                'name': name,
                'age': age
            })
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено")
        cats_info_lst.append({
            'id': None,
            'name': None,
            'age': None
        })
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        cats_info_lst.append({
            'id': None,
            'name': None,
            'age': None
        })

    return cats_info_lst


if __name__ == '__main__':
    cats_info = get_cats_info('cats.txt')
    print(cats_info)

