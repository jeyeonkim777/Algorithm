import sys

def solution(dartResult):
    answer = []
    num = 0

    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            answer.append(num)
        elif dartResult[i] == 'D':
            answer.append(num**2)
        elif dartResult[i] == 'T':
            answer.append(num**3)
        elif dartResult[i] == '*':
            if len(answer) == 1:
                answer[0] = answer[0] * 2
            else:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
        elif dartResult[i] == '#':
            answer[-1] = answer[-1] * -1   
        else:
            if dartResult[i-1:i+1] == '10':
                num = 10
            else:
                num = int(dartResult[i])

    return sum(answer)



dartResult = '1D2S#10S'

print(solution(dartResult))