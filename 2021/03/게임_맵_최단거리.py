from collections import deque

def solution(maps):
    answer = 0
    queue = deque()
    queue.append([0, 0])
    lenx = len(maps)
    leny = len(maps[0])
    visit = [[0]*leny for _ in range(lenx)]
    visit[0][0] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < lenx and 0 <= ty < leny:
                if tx == lenx - 1 and ty == leny - 1:
                    return visit[x][y] + 1
                if visit[tx][ty] == 0 and maps[tx][ty] == 1:
                    visit[tx][ty] = visit[x][y] + 1
                    queue.append([tx, ty])

    return -1




map = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(map))