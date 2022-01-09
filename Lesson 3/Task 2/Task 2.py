# https://codeforces.com/problemset/problem/1490/C

import math as m

def check_num(num):
    border = m.ceil(pow(num, 1/3))
    a = {i**3 for i in range(1, border + 1)}
    
    for i in a:
        if num - i in a:
            return print('YES')
    return print('NO')

def main():
    amount_of_data = int(input())

    for _ in range(amount_of_data):
        number = int(input())
        check_num(number)
        
if __name__ == '__main__':
    main()
