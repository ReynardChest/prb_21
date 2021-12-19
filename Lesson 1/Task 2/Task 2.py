def palindrome_check(input_str, register=False):
    """Определяет, являются ли строка или слова палиндромами.
    исходные данные - массив с True/False
    input_str - строка слов,
    register = False/True - учитывание регистра букв.
    """
    # Учитывание регистра, разделение строки на слова
    if register is False:
        string = str(input_str).lower().split()
    else:
        string = str(input_str).split()

    # Проверка пустой строки
    try:
        if not string:
            raise ValueError('Ошибка: пустая строка!')
    except ValueError as e:
        return print(e)

    # Проверка палиндрома
    output = []
    for word in string:
        if word is word[::-1]:
            output.append(True)
        else:
            output.append(False)
    return output


def main(input_string):
    f = palindrome_check(input_string)
    print(*f)


if __name__ == '__main__':
    main(input('Введите строку: '))
