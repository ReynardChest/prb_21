
def b_indexes(input_str):
    """Функция получает массив индексов b из строки
    """
    b_ind = [b for b, g in enumerate(input_str) if g == 'B']
    return b_ind


def b_indxs_cut(b_indxs, lenght_str):
    """Функция перестаёт учитывать подряд стоящие B в конце массива.
    Выходные данные - новые массив с индексами B и граница, до которой учитываются B
    b_indxs - список с индексами B
    lenght_str - текущая граница, до которой учитываются B
    """
    if b_indxs[len(b_indxs)-1] == lenght_str:  # Если последний элемент массива с индексами b равен индексу границы
        l_b = len(b_indxs)-1  # Начальный индекс последнего элемента массива индексов b
        end_b = len(b_indxs)-1  # Конечный индекс последнего элемента массива индексов b

        while b_indxs[end_b] == b_indxs[end_b-1]+1:
            end_b -= 1  # Определение границы индексов b, после которой b не учитываются

        del b_indxs[end_b:l_b+1]  # Удаление индексов неучитываемых b в конце строки
        lenght_str = lenght_str - (l_b-end_b)-1  # Переопределение границы, после которой не учитываются b
    return b_indxs, lenght_str


def task5_solver(lenght_str, t, input_str):
    """Решает 5 задачу
    lenght_str - длина входной строки
    t - кол-во итераций перестановок
    input_str - строка символов
    """
    b_indxs = b_indexes(input_str)
    n = lenght_str - 1

    for i in range(t):
        c = 0  # Переменная, показывающая итерацию цикла
        for b_ind in b_indxs:

            b_indxs, n = b_indxs_cut(b_indxs, n)

            if not b_indxs:  # Если массив индексов b пуст, прерываем цикл
                break

            # Перестановка мествами b и g + обновление значений индексов b
            if (input_str[b_ind] != input_str[b_ind+1]):
                input_str[b_ind], input_str[b_ind+1] = input_str[b_ind+1], input_str[b_ind]
                b_indxs[c] += 1
                c = c + 1

            else:
                c = c + 1
                continue

    return print(*input_str, sep='')


def main():
    n, t = map(int, input().split())
    a = [c for c in input()]
    task5_solver(n, t, a)


if __name__ == '__main__':
    main()
