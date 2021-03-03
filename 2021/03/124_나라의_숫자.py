def solution(n):
    x = n
    y = 0
    answer = ''

    if n < 3:
        return str(n)
    if n == 3:
        return '4'

    while x / 3 > 1:
        tmp = x

        x = x // 3
        y = tmp % 3

        if y == 0:
            x -= 1
            answer += '4'
        else:
            answer += str(y)

    if x == 3:
        answer += '4'
    else:
        answer += str(x)

    return answer[::-1]

for i in range(40):
    print(solution(i), i)