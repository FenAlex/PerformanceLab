import json
import sys

def get_file_path(prompt, default_path):
    file_path = input(prompt)
    return file_path if file_path else default_path

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: Неверный формат JSON в файле '{file_path}'.")
        return None

def fill_values(tests, value_dict):
    for test in tests:
        test['value'] = value_dict.get(test['id'], "")
        
        if 'values' in test:
            fill_values(test['values'], value_dict)

def create_result_file(tests, values, output_path):
    value_dict = {value['id']: value['value'] for value in values}
    
    fill_values(tests['tests'], value_dict)
    
    with open(output_path, 'w') as f:
        json.dump({"tests": tests}, f, indent=4)

def main():
    test_file_path = sys.argv[1] if len(sys.argv) > 1 else './task3/tests.json'
    values_file_path = sys.argv[2] if len(sys.argv) > 2 else './task3/values.json'
    result_file_path = sys.argv[3] if len(sys.argv) > 3 else './task3/result.json'
    
    if len(sys.argv) < 4:
        test_file_path = get_file_path("Введите путь к файлу с тестами: ", test_file_path)
        values_file_path = get_file_path("Введите путь к файлу с значениями: ", values_file_path)
        result_file_path = get_file_path("Введите путь к файлу для сохранения результата: ", result_file_path)

    tests = load_json(test_file_path)
    values = load_json(values_file_path)

    if tests is not None and values is not None:
        create_result_file(tests, values['values'], result_file_path)
        print(f"Результат успешно сохранен в '{result_file_path}'.")

if __name__ == "__main__":
    main()
