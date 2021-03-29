def solution(s):
    s = list(map(int, s.split(' ')))
    s.sort()
    answer = ''
    answer += str(s[0]) + ' ' + str(s[-1])
    return answer


print(solution("-4 -2 4 -1 3 33"))