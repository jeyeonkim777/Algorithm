def solution(number, k):
    answer = ''
    idx = 0
    cnt = k

    while True:
        x = ''
        y = 0
        for i in range(idx, idx+k+1):
            if number[i] == '9':
                x = number[i]
                y = i
                break
            elif x < number[i]:
                x = number[i]
                y = i
            
        answer += x
        k -= (y - idx)
        idx = y + 1
        
        if k == 0:
            if idx < len(number):
                return answer + number[idx:]
            else:
                return answer

        elif k == cnt and idx == len(number) - 1:
            return answer



print(solution('99998', 4))