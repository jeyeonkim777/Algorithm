import sys
from collections import Counter

def solution(participant, completion):

    arr = participant + completion

    people = Counter(arr)

    for k, v in people.items():
        if v % 2 == 1:
            return k

print(solution(['leo', 'kiki', 'eden'], ['leo', 'kiki']))