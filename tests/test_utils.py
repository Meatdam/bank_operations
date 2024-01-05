import pytest
from src.utils import get_data_for_sort, get_date_format


def test_get_data_for_sort():
    assert get_data_for_sort({"date": "2019-07-13T18:51:29.313309"}) == "2019-07-13T18:51:29.313309"


def test_get_date_format():
    assert get_date_format()


def test_load_json_operations_error():
    with pytest.raises(TypeError):
        get_data_for_sort('привет')
