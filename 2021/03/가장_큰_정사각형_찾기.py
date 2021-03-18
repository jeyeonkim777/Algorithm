from collections import deque

def solution(board):
    answer = 0

    x = len(board)
    y = len(board[0])

    for i in range(x):
        for j in range(y):

            if board[i][j] == 1:

                queue = deque()
                cnt = 1
                flag = True
                queue.append([i, j])

                while True:

                    qlen = len(queue)

                    while qlen:
                        px, py = queue.popleft()

                        if px+1 >= x or py+1 >= y:
                            flag = False
                            break

                        if board[px+1][py] == 0 or board[px][py+1] == 0 or board[px+1][py+1] == 0:
                            flag = False
                            break

                        else:
                            queue.append([px+1, py])
                            queue.append([px, py+1])
                            queue.append([px+1, py+1])

                        qlen -= 1

                    if flag == False:
                        break
                    else:
                        cnt += 1

                if cnt > answer:
                    answer = cnt

    return answer ** 2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))