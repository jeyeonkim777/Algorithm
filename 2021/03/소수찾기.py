import itertools
import math

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    numbers_npr = []
    prime = []

    for i in range(len(numbers)):
        numbers_npr += list(itertools.permutations(numbers, i+1))

    for i in range(len(numbers_npr)):
        num = int(''.join(numbers_npr[i]))
        if num in prime:
            continue
        if num == 0 or num == 1:
            continue
        else:
            flag = True
            x = int(math.sqrt(num))
            for j in range(2, x+1):
                if num % j == 0:
                    flag = False
                    break
            if flag == True:
                prime.append(num)
                answer += 1
    return answer

print(solution('017'))


