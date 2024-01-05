import json
import os
from config import ROOT_DIR
from datetime import datetime
import re

OPERATION_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')


def load_json_operations():
    """
    Забирает Json файл и выводит только успешные операции
    """
    with open(OPERATION_PATH, encoding='UTF-8') as file:
        operation_files = json.load(file)
        operations_list = []
        for operation in operation_files:
            if operation == {}:
                continue
            if operation["state"] == "EXECUTED":
                operations_list.append(operation)
        return operations_list


operations_user = load_json_operations()


def get_data_for_sort(value):
    """
    Сортирует данные по дате
    """
    return value['date']


def get_date_format():
    """
    Редактирует вывод оппераций, скрывает счет от пользователей, выводит последние 5 выполненных операций,
    номера счетов, сумма, валюта
    """
    result_operation = []
    sort_listing = sorted(operations_user, key=get_data_for_sort, reverse=True)
    sort_list = sort_listing[0:5]
    for i in sort_list:
        format_date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f")
        format_to_check = re.findall('....', i['to'])
        check_to_index = format_to_check[4:]
        check_tuple = check_to_index[0].replace(check_to_index[0], "**"), check_to_index[1]
        to_check = ''.join(list(check_tuple))
        if i["description"] == "Открытие вклада":
            i["from"] = f"Счет пользователя: {i['to'][5:]}"
        from_format_check = i['from'].split()
        from_format_check_copy = from_format_check.copy()
        del from_format_check_copy[-1]
        from_check_spaces = re.findall('....', from_format_check[-1])
        from_cipher_check = (from_check_spaces[0], from_check_spaces[1][0:2] + '**',
                             from_check_spaces[2].replace(from_check_spaces[2], "****"), from_check_spaces[3:])
        frpm_join_cipher_check = ' '.join(from_cipher_check[3])
        index_check = (f"{' '.join(from_format_check_copy)} {' '.join(list(from_cipher_check[0:3]))} "
                       f"{frpm_join_cipher_check}")
        date = (f"{format_date:%d.%m.%Y} {i['description']}\n{index_check} --> "
                f"{to_check}\n{i['operationAmount']['amount']} "
                f"{i['operationAmount']['currency']['name']}")
        result_operation.append(date)
    return '\n\n'.join(result_operation)
