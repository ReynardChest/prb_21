def unic_symb_count(input_str, register=False):
    """Определяет количество уникальных символов в стороке.
    исходные данные - массив с True/False
    input_str - строка слов,
    register = False/True - учитывание регистра букв.
    """
    # Учитывание регистра, разделение строки на слова
    if register is False:
        string = str(input_str).lower()
    else:
        string = str(input_str)

    # Проверка пустой строки
    try:
        if not string:
            raise ValueError('Ошибка: пустая строка!')
    except ValueError as e:
        return print(e)

    dic = dict.fromkeys(string, 0)

    for symbol in string:
        dic[symbol] += 1

    return list(dic.values()).count(1)


def main(input_string):
    c = unic_symb_count(input_string)
    print('Кол-во уникальных символов:', c)


if __name__ == '__main__':
    main(input('Введите строку: '))
