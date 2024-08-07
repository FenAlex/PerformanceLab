def get_circle_data():
    while True:
        circle_file = input("Введите путь к файлу с данными о круге: ")
        if not circle_file:
            circle_file = './task2/circle.txt'
        
        try:
            with open(circle_file, 'r') as f:
                data = f.readlines()
                x, y = map(float, data[0].strip().split())
                radius = float(data[1].strip())
            return (x, y, radius)
        except FileNotFoundError:
            print(f"Ошибка: Файл '{circle_file}' не найден. Пожалуйста, попробуйте снова.")
        except ValueError:
            print("Ошибка: Неверный формат данных в файле. Убедитесь, что координаты и радиус указаны правильно. Попробуйте снова.")
        except Exception as e:
            print(f"Произошла ошибка: {e}. Пожалуйста, попробуйте снова.")

def get_points_data():
    while True:
        points_file = input("Введите путь к файлу с координатами точек: ")
        if not points_file:
            points_file = './task2/dot.txt'
        
        try:
            points = []
            with open(points_file, 'r') as f:
                for line in f:
                    x, y = map(float, line.strip().split())
                    points.append((x, y))
            return points
        except FileNotFoundError:
            print(f"Ошибка: Файл '{points_file}' не найден. Пожалуйста, попробуйте снова.")
        except ValueError:
            print("Ошибка: Неверный формат данных в файле. Убедитесь, что координаты указаны правильно. Попробуйте снова.")
        except Exception as e:
            print(f"Произошла ошибка: {e}. Пожалуйста, попробуйте снова.")


def point_position(circle, point):
    x_center, y_center, radius = circle
    x_point, y_point = point
    distance_squared = (x_point - x_center) ** 2 + (y_point - y_center) ** 2
    radius_squared = radius ** 2

    if distance_squared < radius_squared:
        return 1  # Точка внутри
    elif distance_squared == radius_squared:
        return 0  # Точка на окружности
    else:
        return 2  # Точка снаружи

def main():
    circle = get_circle_data()
    points = get_points_data()

    results = []
    for point in points:
        result = point_position(circle, point)
        results.append(result)

    print("Результаты:")
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
