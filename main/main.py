from src.utils import *

load_json = load_json_operations()
sort_list = sort_list_operations(load_json)
format_date = format_date_operations(sort_list)
format_check = get_format_check(sort_list)
format_card = get_format_card(sort_list)

for operation in range(len(sort_list)):
    print(f"{format_date[operation]} {sort_list[operation]['description']}\n{format_card[operation]} --> "
          f"{format_check[operation]}\n{sort_list[operation]['operationAmount']['amount']} "
          f"{sort_list[operation]['operationAmount']['currency']['name']}\n")
