# https://codeforces.com/problemset/problem/1490/C

import math as m


def check_num(num):
    n = 0
    for i in range(1, num+1):
        n += 2**i      
    return n


def main():
    num = int(input())

    print(check_num(num))


if __name__ == '__main__':
    main()
