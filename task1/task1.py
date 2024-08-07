def get_path(array, m):
    path = []
    i = 0

    while True:
        path.append(array[i])
        i = (i + m) % len(array)
        if i == 0:
            break

    return path

n = int(input("Введите число n: "))
m = int(input("Введите число m: "))

array = list(range(1, n + 1))

result = get_path(array, m-1)

print(result)