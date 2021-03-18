def solution(s):
    answer = True
    arr = []

    if s[0] == ')':
        return False

    for i in range(len(s)):
        if len(arr) == 0:
            arr.append(s[i])
        else:
            if s[i] == '(':
                arr.append(s[i])
            else:
                arr.pop()

    if len(arr) > 0:
        return False

    else:
        return True