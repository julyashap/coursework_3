from src.utils import (get_list_from_json, get_set_up_transactions, get_executed_transactions, convert_date_to_datetime,
                       get_sort_transactions_by_date, convert_card_number, convert_account_number, get_card_number,
                       get_bank_name, select_converting, convert_date, get_output)
import pytest
import datetime


@pytest.fixture
def get_test_operations_file():
    return "test_operations.json"


def test_get_list_from_json(get_test_operations_file):
    expected_result = [
        {},
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro Card 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293",
            "operationAmount": {
                "amount": "3348.98",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "to": "Visa Gold 9447344650495960"
        },
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2018-04-14T19:35:28.978265",
            "operationAmount": {
                "amount": "96995.73",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 27248529432547658655",
            "to": "Счет 97584898735659638967"
        },
        {
            "id": 541945802,
            "state": "CANCELED",
            "date": "2019-07-12T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 64686473678894779589",
            "to": "Maestro Card 1596837868705199"
        },
        {
            "id": 108066781,
            "state": "EXECUTED",
            "date": "2019-06-21T12:34:06.351022",
            "operationAmount": {
                "amount": "25762.92",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90817634362091276762"
        },
        {
            "id": 100392079,
            "state": "EXECUTED",
            "date": "2019-03-03T03:13:18.622393",
            "operationAmount": {
                "amount": "44493.45",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 6319351940209800",
            "to": "Счет 14073196441261107791"
        },
        {
            "id": 556488059,
            "state": "CANCELED",
            "date": "2019-05-17T01:50:00.166954",
            "operationAmount": {
                "amount": "74604.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "МИР 8021883699486544",
            "to": "Visa Gold 8702717057933248"
        }
    ]

    assert get_list_from_json(get_test_operations_file) == expected_result
    assert type(get_list_from_json(get_test_operations_file)) == list


def test_get_set_up_transactions(get_test_operations_file):
    expected_result = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro Card 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293",
            "operationAmount": {
                "amount": "3348.98",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "to": "Visa Gold 9447344650495960"
        },
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2018-04-14T19:35:28.978265",
            "operationAmount": {
                "amount": "96995.73",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 27248529432547658655",
            "to": "Счет 97584898735659638967"
        },
        {
            "id": 541945802,
            "state": "CANCELED",
            "date": "2019-07-12T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 64686473678894779589",
            "to": "Maestro Card 1596837868705199"
        },
        {
            "id": 108066781,
            "state": "EXECUTED",
            "date": "2019-06-21T12:34:06.351022",
            "operationAmount": {
                "amount": "25762.92",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90817634362091276762"
        },
        {
            "id": 100392079,
            "state": "EXECUTED",
            "date": "2019-03-03T03:13:18.622393",
            "operationAmount": {
                "amount": "44493.45",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 6319351940209800",
            "to": "Счет 14073196441261107791"
        },
        {
            "id": 556488059,
            "state": "CANCELED",
            "date": "2019-05-17T01:50:00.166954",
            "operationAmount": {
                "amount": "74604.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "МИР 8021883699486544",
            "to": "Visa Gold 8702717057933248"
        }
    ]

    assert get_set_up_transactions(get_test_operations_file) == expected_result


def test_get_executed_transactions(get_test_operations_file):
    expected_result = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro Card 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293",
            "operationAmount": {
                "amount": "3348.98",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "to": "Visa Gold 9447344650495960"
        },
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2018-04-14T19:35:28.978265",
            "operationAmount": {
                "amount": "96995.73",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 27248529432547658655",
            "to": "Счет 97584898735659638967"
        },
        {
            "id": 108066781,
            "state": "EXECUTED",
            "date": "2019-06-21T12:34:06.351022",
            "operationAmount": {
                "amount": "25762.92",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90817634362091276762"
        },
        {
            "id": 100392079,
            "state": "EXECUTED",
            "date": "2019-03-03T03:13:18.622393",
            "operationAmount": {
                "amount": "44493.45",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 6319351940209800",
            "to": "Счет 14073196441261107791"
        }
    ]

    assert get_executed_transactions(get_test_operations_file) == expected_result


def test_convert_data_to_datetime():
    assert convert_date_to_datetime('2019-08-26T10:50:58.294041') == datetime.date(2019, 8, 26)
    assert str(type(convert_date_to_datetime('2019-08-26T10:50:58.294041'))) == "<class 'datetime.date'>"


def test_get_sort_transactions_by_date(get_test_operations_file):
    expected_result = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro Card 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 108066781,
            "state": "EXECUTED",
            "date": "2019-06-21T12:34:06.351022",
            "operationAmount": {
                "amount": "25762.92",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90817634362091276762"
        },
        {
            "id": 100392079,
            "state": "EXECUTED",
            "date": "2019-03-03T03:13:18.622393",
            "operationAmount": {
                "amount": "44493.45",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 6319351940209800",
            "to": "Счет 14073196441261107791"
        },
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293",
            "operationAmount": {
                "amount": "3348.98",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "to": "Visa Gold 9447344650495960"
        },
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2018-04-14T19:35:28.978265",
            "operationAmount": {
                "amount": "96995.73",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 27248529432547658655",
            "to": "Счет 97584898735659638967"
        }
    ]

    assert get_sort_transactions_by_date(get_test_operations_file) == expected_result
    assert len(get_sort_transactions_by_date(get_test_operations_file)) == 5


def test_convert_card_number():
    assert convert_card_number("8702717057933248") == "8702 71** **** 3248"


def test_convert_account_number():
    assert convert_account_number("28429442875257789335") == "**9335"


def test_get_card_number():
    assert get_card_number("Visa Gold 8702717057933248") == "8702717057933248"
    assert get_card_number("Visa Gold") is None


def test_get_bank_name():
    assert get_bank_name("Visa Gold 8702717057933248").strip() == "Visa Gold"
    assert get_bank_name("Счет 28429442875257789335").strip() == "Счет"
    assert get_bank_name("8702717057933248") == ""


def test_select_converting():
    assert select_converting("Visa Gold 8702717057933248") == "8702 71** **** 3248"
    assert select_converting("Счет 28429442875257789335") == "**9335"


def test_convert_date():
    assert convert_date('2019-08-26T10:50:58.294041') == '26.08.2019'
    assert str(type(convert_date('2019-08-26T10:50:58.294041'))) == "<class 'str'>"


def test_get_output(get_test_operations_file):
    expected_result = """26.08.2019 Перевод организации
Maestro Card  1596 83** **** 5199 -> Счет ****************9589
31957.58 руб.

21.06.2019 Открытие вклада
Счет ****************6762
25762.92 руб.

03.03.2019 Перевод с карты на счет
Visa Classic  6319 35** **** 9800 -> Счет ****************7791
44493.45 USD

29.11.2018 Перевод с карты на карту
MasterCard  3152 47** **** 5065 -> Visa Gold  9447 34** **** 5960
3348.98 USD

14.04.2018 Перевод организации
Счет ****************8655 -> Счет ****************8967
96995.73 руб.

"""

    assert get_output(get_test_operations_file) == expected_result
