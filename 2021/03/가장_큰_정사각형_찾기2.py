def solution(board):
    answer = 0

    x = len(board)
    y = len(board[0])

    visit = [[0]*(y+1) for _ in range(x+1)]

    for i in range(x):
        for j in range(y):
            visit[i][j] = board[i][j]

    for i in range(x):
        for j in range(y):
            if visit[i][j] != 0:
                if visit[i+1][j] == 0 or visit[i][j+1] == 0 or visit[i+1][j+1] == 0:
                    continue
                visit[i+1][j+1] = min(visit[i+1][j], visit[i][j+1], visit[i][j]) + 1


    for i in range(x+1):
        if max(visit[i]) > answer:
            answer = max(visit[i])

    return answer**2


print(solution([[1,1,1],[1,0,1],[1,1,1]]))