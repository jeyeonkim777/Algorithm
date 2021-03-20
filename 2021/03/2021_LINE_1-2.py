def solution(inp_str):
    answer = []
    obj = {}
    cnt = [0, 0, 0, 0]

    if 8 > len(inp_str) or len(inp_str) > 15:
        answer.append(1)

    for i in inp_str:
        if i in '()-_=+':
            if 2 not in answer:
                answer.append(2)
        
        else:
            if i in '~!@#$%^&*':
                cnt[0] += 1
            elif i in '0123456789':
                cnt[1] += 1
            elif 65 <= ord(i) <= 90:
                cnt[2] += 1
            else:
                cnt[3] += 1

        if i not in obj:
            obj[i] = 1
        else:
            obj[i] += 1

    cnt.sort()
    if cnt[0] == 0 and cnt[1] == 0:
        answer.append(3)
    
    for key, value in obj.items():
        if value > 3:
            str_list = list(filter(lambda x: inp_str[x] == key, range(len(inp_str))))
            tmp = 1
            for i in range(len(str_list)-1):
                if str_list[i] + 1 == str_list[i+1]:
                    tmp += 1
                    if tmp >= 4:
                        answer.append(4)
                        break
                else:
                    tmp = 0
            
            if tmp >= 4:
                break

    if max(obj.values()) > 4:
        answer.append(5)

    if len(answer) == 0:
        return [0]
    else:
        return answer


print(solution("CaCbCgCdC888834A99999"))