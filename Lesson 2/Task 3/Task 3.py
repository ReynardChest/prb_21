# https://codeforces.com/problemset/problem/1613/C

def Poison_damage_search(dragon_hp, poison_ticks, remaining_attacks):

    if dragon_hp < remaining_attacks:
        return 1

    sum_damage = 0
    for curr_damage in poison_ticks:
        if curr_damage > ((dragon_hp-sum_damage)//remaining_attacks):
            break
        sum_damage += curr_damage
        remaining_attacks -= 1
    return (0-(sum_damage-dragon_hp)//remaining_attacks)


def main():
    amount_of_data = int(input())

    dragon_raids = []
    for _ in range(amount_of_data):
        amount_attacks, dragon_hp = map(int, input().split())
        attacks = tuple(map(int, input().split()))
        poison_ticks = [attacks[curr] - attacks[curr-1] for curr in range(1, len(attacks))]
        poison_ticks.sort()
        dragon_raids.append(tuple([amount_attacks, dragon_hp, poison_ticks]))

    for curr_try in dragon_raids:
        amount_attacks = curr_try[0]
        dragon_hp = curr_try[1]
        poison_ticks = curr_try[2]

        return(print(Poison_damage_search(dragon_hp, poison_ticks, amount_attacks)))


if __name__ == '__main__':
    main()
