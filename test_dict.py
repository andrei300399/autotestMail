import pytest


def test_dict_key_number_equal_item():
    dict_numb = {'1': 1, 'm': 2}
    for i in dict_numb:
        try:
            assert dict_numb[i] == int(i)
        except ValueError:
            pass


@pytest.mark.parametrize('item', [{'0': 0},{'100': -100}, {'50': 50}])
def test_dict_equal_absolute(item):
    key_num = list(item.keys())[0]
    assert int(key_num) == abs(item[key_num])

def test_dict_first_letter():
    dict_city = {'M': 'Moscow', 'B': 'Berlin'}
    for i in dict_city:
        assert dict_city[i][0] == i


