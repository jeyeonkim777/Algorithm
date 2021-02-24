import sys

def solution(d, budget):

    d.sort()
    num = 0

    for i in range(len(d)):
        num += d[i]
        
        if num > budget:
            return i

    return len(d)