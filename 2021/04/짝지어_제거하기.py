def solution(s):
    answer = 0
    arr = [s[0]]

    for i in range(1, len(s)):
        if len(arr) == 0:
            arr.append(s[i])
        elif arr[-1] != s[i]:
            arr.append(s[i])
        else:
            arr.pop()    

    if len(arr) == 0:
        return 1
    else:
        return 0