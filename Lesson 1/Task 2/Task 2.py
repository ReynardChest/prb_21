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
    else:
        # Проверка палиндрома
        output = []
        for word in string:
            if word == word[::-1]:
                output.append(True)
            else:
                output.append(False)
        return print(*output)


def main(input_string):
    palindrome_check(input_string)


if __name__ == '__main__':
    main(input('Введите строку: '))
