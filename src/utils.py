import json
from datetime import date


def get_list_from_json():
    """
    Возвращает список транзакций клиента
    """
    with open("../operations.json") as file:
        customer_transactions = json.load(file)
    return customer_transactions


def get_set_up_transactions():
    """

    """
    customer_transactions = get_list_from_json()
    customized_transactions = customer_transactions.copy()

    for trans in customized_transactions:
        if trans == {}:
            customized_transactions.remove(trans)

    return customized_transactions


def get_executed_transactions():
    """
    Возвращает список успешно завершенных транзакций
    """
    customer_transactions = get_set_up_transactions()

    executed_transactions = [trans for trans in customer_transactions if trans['state'] == 'EXECUTED']

    return executed_transactions


def convert_date_to_datetime(thedate):
    """

    """
    new_date = date(int(thedate[:4]), int(thedate[5:7]), int(thedate[8:10]))

    return new_date


def get_sort_transactions_by_date():
    """

    """
    customer_transactions = get_executed_transactions()
    sorted_transactions = sorted(customer_transactions,
                                 key=lambda trans: convert_date_to_datetime(trans.get("date")),
                                 reverse=True)

    return sorted_transactions[:5]


def convert_card_number(card_number):
    """

    """
    card_number_converted = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    return card_number_converted


def convert_account_number(account_number):
    """

    """
    account_number_converted = ""
    count = 0

    while count < len(account_number) - 4:
        account_number_converted += "*"
        count += 1

    account_number_converted += account_number[-4:]

    return account_number_converted


def get_card_number(card_number):
    card_number_splitted = card_number.split()

    for part in card_number_splitted:
        if part.isdigit():
            return part


def get_bank_name(bank_name):
    bank_name_splitted = bank_name.split()

    if bank_name_splitted[0] == "Счет":
        return bank_name_splitted[0]
    else:
        card_name = ""

        for part in bank_name_splitted:
            if part.isalpha():
                card_name += part + " "

        return card_name


def select_converting(bank_number):
    bank_number_splitted = bank_number.split()

    if bank_number_splitted[0] == "Счет":
        return convert_account_number(bank_number_splitted[1])
    else:
        return convert_card_number(get_card_number(bank_number))


def convert_date(thedate):
    """

    """
    new_date = convert_date_to_datetime(thedate)

    date_converted = new_date.strftime("%d.%m.%Y")

    return date_converted


def get_output():
    """

    """
    customer_transactions = get_sort_transactions_by_date()
    result_output = ""

    for trans in customer_transactions:
        trans_to = get_bank_name(trans['to'])

        if 'from' in trans.keys():
            trans_from = get_bank_name(trans['from'])
            result_output += (f"{convert_date(trans['date'])} {trans['description']}\n"
                              f"{trans_from} {select_converting(trans['from'])} "
                              f"-> {trans_to} {select_converting(trans['to'])}\n"
                              f"{trans['operationAmount']['amount']} "
                              f"{trans['operationAmount']['currency']['name']}\n")
        else:
            result_output += (f"{convert_date(trans['date'])} {trans['description']}\n"
                              f"{trans_to} {select_converting(trans['to'])}\n"
                              f"{trans['operationAmount']['amount']} "
                              f"{trans['operationAmount']['currency']['name']}\n")

        result_output += "\n"

    return result_output
