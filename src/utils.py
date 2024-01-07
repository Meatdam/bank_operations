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


def sort_list_operations(operations_list):
    """
    Сортирует json по дате и выводит последние 5 банковский операций
    """
    sort_listing = sorted(operations_list, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"),
                          reverse=True)
    sort_list = sort_listing[0:5]
    return sort_list


def format_date_operations(format_date):
    """
    Выводит дату в формате (День, месяц, год)
    """
    date_list = []
    for item_data in format_date:
        date = datetime.strptime(item_data["date"], "%Y-%m-%dT%H:%M:%S.%f")
        date_format = f"{date:%d.%m.%Y}"
        date_list.append(date_format)
    return date_list


def get_format_check(checks_to):
    """
    Выводит счет в замаскированом формате последние 4 цифры '**счет'
    """
    list_check = []
    for check in checks_to:
        format_to_check = re.findall('....', check['to'])
        check_to_index = format_to_check[4:]
        check_tuple = check_to_index[0].replace(check_to_index[0], "**"), check_to_index[1]
        to_check = ''.join(list(check_tuple))
        list_check.append(to_check)
    return list_check


def get_format_card(card_from):
    """
    Выводит номер карты в замаскированом формате '123* **** 2333'
    и делит на пробелы через каждые 4 числа
    """
    list_card = []
    for card in card_from:
        if card["description"] == "Открытие вклада":
            card["from"] = f"Счет пользователя: {card['to'][5:]}"
        from_format_check = card['from'].split()
        from_format_check_copy = from_format_check.copy()
        del from_format_check_copy[-1]
        from_check_spaces = re.findall('....', from_format_check[-1])
        from_cipher_check = (from_check_spaces[0], from_check_spaces[1][0:2] + '**',
                             from_check_spaces[2].replace(from_check_spaces[2], "****"), from_check_spaces[3:])
        frpm_join_cipher_check = ' '.join(from_cipher_check[3])
        list_card.append(f"{' '.join(from_format_check_copy)} {' '.join(list(from_cipher_check[0:3]))} "
                         f"{frpm_join_cipher_check}")
    return list_card
