import sys

def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        sys.exit(1)
    except ValueError:
        print("Ошибка: Неверный формат данных в файле.")
        sys.exit(1)

def min_moves_to_equal(nums):
    median = sorted(nums)[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else input("Введите путь к файлу с числами: ")
    
    if not file_path:
        file_path = './task4/numbers.txt'

    nums = read_numbers_from_file(file_path)
    moves = min_moves_to_equal(nums)
    print(f"Минимальное количество ходов: {moves}")

if __name__ == "__main__":
    main()
