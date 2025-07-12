def get_cats_info(path: str) -> list[dict]:
    cats_info = []

    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                id, name, age = line.split(',')
                cats_info.append({
                    'id': id,
                    'name': name,
                    'age': int(age)
                })
    except FileNotFoundError:
        print('File not found or not readable')

    return cats_info

print(get_cats_info('data/cats.csv'))