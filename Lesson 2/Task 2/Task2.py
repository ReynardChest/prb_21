# https://codeforces.com/problemset/problem/1015/C
def Maxmin_songs_weight(memory, songs):

    max_songs_weight = 0
    min_songs_weight = 0
    for song_char in songs:
        max_songs_weight += song_char[0]
        min_songs_weight += song_char[1]
    return max_songs_weight, min_songs_weight


def num_cut_songs(weight, memory, songs):
    i = 0
    while weight > memory:
        weight -= songs[i][2]
        i += 1
    return i


def main():
    num_songs, flash_mem = map(int, input().split())

    songs = []
    for _ in range(num_songs):
        num1, num2 = map(int, input().split())
        songs.append(tuple([num1, num2, num1-num2]))

    Max_w, min_w = Maxmin_songs_weight(flash_mem, songs)

    if min_w <= flash_mem:
        songs = sorted(songs, key=lambda x: x[2], reverse=True)
        zip_songs = num_cut_songs(Max_w, flash_mem, songs)
        print(zip_songs)

    else:
        print('-1')


if __name__ == '__main__':
    main()
