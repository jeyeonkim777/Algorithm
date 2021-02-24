import sys

def solution(s, n):

    arr = []

    for i in s:
        strToInt = ord(i)     
        tmp = 0

        if strToInt == 32:
            arr.append(' ')
        else:
            if strToInt <= 90:
                if strToInt + n > 90:
                    tmp = strToInt + n - 90
                    arr.append(chr(65 + tmp - 1)) 
                else:
                    arr.append(chr(strToInt + n))
            else:
                if strToInt + n > 122:
                    tmp = strToInt + n - 122
                    arr.append(chr(97 + tmp - 1)) 
                else:
                    arr.append(chr(strToInt + n))


    answer = ''.join(arr)
    return answer

print(solution('Z', 1))