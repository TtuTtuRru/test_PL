import sys
import json

def load_json(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(file_path, data):

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def fill_report(tests, values_dict):

    if isinstance(tests, dict):
        if 'id' in tests and tests['id'] in values_dict:
            tests['value'] = values_dict[tests['id']]
        for key in tests:
            fill_report(tests[key], values_dict)
    elif isinstance(tests, list):
        for item in tests:
            fill_report(item, values_dict)
    return tests

def main():

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    values_data = load_json(values_path)
    tests_data = load_json(tests_path)

    values_dict = {item['id']: item['value'] for item in values_data['values']}

    report = fill_report(tests_data, values_dict)

    save_json(report_path, report)

if __name__ == "__main__":
    main()