def solution(n):
    answer = 0

    lstn = list(str(n))

    if '0' not in lstn:
        return '10' + str(n)[1:]

    for i in range(len(lstn)-1):
        if lstn[i] == '0' and lstn[i+1] == '1':
            lstn[i] = '1'




print(solution(1111))