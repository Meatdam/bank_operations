import pytest
from src.utils import *


def test_get_data_for_sort():
    assert format_date_operations([{"date": "2019-08-26T10:50:58.294041"}]) == ['26.08.2019']
    assert sort_list_operations([{"date": "2019-08-26T10:50:58.294041"}]) == [{"date": "2019-08-26T10:50:58.294041"}]
    assert get_format_check([{"to": "Счет 64686473678894779589"}]) == ['**7958']
    assert (get_format_card([{"description": "Перевод организации", "from": "Maestro 1596837868705199"}]) ==
            ['Maestro 1596 83** **** 5199'])


def test_load_json_operations_error():
    with pytest.raises(TypeError):
        load_json_operations('привет')
        format_date_operations("2000.22.14")
