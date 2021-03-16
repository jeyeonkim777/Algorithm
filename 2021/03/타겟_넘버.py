from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([0, 0])
    dx = [-1, 1]

    while queue:
        number, idx = queue.popleft()
        if idx == len(numbers):
            if number == target:
                answer += 1
        else:
            for i in dx:
                tx = i * numbers[idx]
                queue.append([number+tx, idx+1])

    return answer

print(solution([1, 1, 1, 1, 1], 3))