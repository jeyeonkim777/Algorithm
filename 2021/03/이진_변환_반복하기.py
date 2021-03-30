def solution(s):

    answer = [0, 0]

    while True:
        if s == '1':
            break

        len_s = len(s)

        list_s = s.split('0')
        tmp = ''.join(list_s)
        s = format(len(tmp), 'b')

        answer[0] += 1
        answer[1] += (len_s - len(tmp))

    return answer


print(solution("110010101001"))