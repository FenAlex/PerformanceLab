import sys

def get_path(array, m):
    path = []
    i = 0

    while True:
        path.append(array[i])
        i = (i + m) % len(array)
        if i == 0:
            break

    return path

# Проверка наличия аргументов командной строки
if len(sys.argv) == 3:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
elif len(sys.argv) == 1:
    n = int(input("Пожалуйста, введите длину массива: "))
    m = int(input("Пожалуйста, введите шаг: "))

# Получение значений n и m из аргументов командной строки

array = list(range(1, n + 1))

result = get_path(array, m - 1)

output = ''.join(map(str, result))

print(output)