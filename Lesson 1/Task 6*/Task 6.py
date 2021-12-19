def num_ord_summ(string):

    number = [int(c) for c in str(string)]

    return (lambda x: sum(x))(number)


def main():
    string = input('Введите число: ')
    print(num_ord_summ(string))


if __name__ == '__main__':
    main()
