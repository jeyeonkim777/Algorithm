def solution(s):
    answer = 10000

    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2 + 1):
        start = 0
        idx = i
        cnt = 0
        result = 0

        # print('---', i, '---')
        while True:
            # print(s[start:start+idx], s[start+idx:start+idx*2], result)
            if s[start:start+idx] == s[start+idx:start+idx*2]:
                cnt += 1
            else:
                if 99 <= cnt:
                    result += 3 + i
                elif 9 <= cnt:
                    result += 2 + i
                elif 0 < cnt:
                    result += 1 + i
                else:
                    result += i
                cnt = 0
            
            start += idx

            if start + idx > len(s):
                result += len(s[start:])
                break
            elif start == len(s):
                result += len(s[start:]) + len(str(cnt+1))
        
        if answer > result:
            answer = result

    return answer



print(solution('a'))