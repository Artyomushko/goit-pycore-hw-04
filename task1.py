def total_salary(path: str) -> tuple[float, float]:
    sum_salary = 0
    workers = 0

    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, salary = line.split(',')
                sum_salary += float(salary)
                workers += 1
    except FileNotFoundError:
        print('File not found or not readable')

    if workers == 0:
        return 0, 0

    return sum_salary, sum_salary / workers

print(total_salary('data/salary.csv'))