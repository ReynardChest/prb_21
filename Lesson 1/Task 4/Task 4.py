def task4_solver(end_pos, portals, start_pos=0):
    """Решает 4 задачу
    start_pos - ячейка старта
    end_pos - ячейка, на которой должны закончить
    portals - массив со связями ячеек
    """
    curr_pos = start_pos

    while curr_pos < end_pos-1:
        curr_pos = curr_pos + portals[curr_pos]

    if curr_pos == end_pos-1:
        return(print('YES'))
    else:
        return(print('NO'))


def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    task4_solver(t, a)


if __name__ == '__main__':
    main()
