def count_one(nb):
    cnt = 0
    for i in nb:
        if i == '1':
            cnt += 1

    return cnt


def solution(n):
    nb = format(n, 'b')
    n_num = count_one(nb)

    while True:
        n += 1
        nb = format(n, 'b')
        cnt_num = count_one(nb)

        if cnt_num == n_num:
            break

    return n


print(solution(15))