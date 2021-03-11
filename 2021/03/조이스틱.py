from collections import deque


def solution(name):
    answer = 0
    queue = deque()
    
    dx = [1, -1]
    visit = 'A'*len(name)
    queue.append([0, 0, visit])
    
    while queue:
        x, answer, visit = queue.popleft()

        if visit == name:
            return answer - 1

        if ord(name[x]) <= 77:
            answer += (ord(name[x]) - 65)
        else:
            answer += (90 - ord(name[x]) + 1)

        if visit[x] != name[x]:
            visit = list(visit)
            visit[x] = name[x]
            visit = ''.join(visit)

        for i in dx:
            tx = x + i

            if tx < len(name) or tx >= -len(name):
                queue.append([tx, answer+1, visit])


print(solution('JAZ'))