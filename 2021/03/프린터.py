from collections import deque
import copy

def solution(priorities, location):
    arr = deque([i for i in priorities])
    tmp = location
    answer = 0

    while len(arr):

        if arr[0] >= max(arr):
            arr.popleft()
            answer += 1

            if tmp == 0:
                return answer
                
        else:
            arr.append(arr[0])
            arr.popleft()

        if tmp == 0:
            tmp = len(arr) - 1
        else:
            tmp -= 1

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))