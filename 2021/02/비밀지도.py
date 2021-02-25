import sys

def solution(n, arr1, arr2):
    
    visit = [''] * n

    for i in range(n):
        tmp1 = str(format(arr1[i], 'b'))
        tmp2 = str(format(arr2[i], 'b'))
        
        if arr1[i] < 2**(n-1):
            while len(tmp1) < n:
                tmp1 = '0' + tmp1
        
        if arr2[i] < 2**(n-1):
            while len(tmp2) < n:
                tmp2 = '0' + tmp2

        for j in range(n):
            if tmp1[j] == '1' or tmp2[j] == '1':
                visit[i] += '#'
            else:
                visit[i] += ' '

    return visit

    
n =	6
arr1 =	[46, 33, 33 ,22, 31, 50]
arr2 =	[27 ,56, 19, 14, 14, 10]
        

        
# n =	5
# arr1 =	[9, 20, 28, 18, 11]
# arr2 =	[30, 1, 21, 17, 28]


print(solution(n, arr1, arr2))