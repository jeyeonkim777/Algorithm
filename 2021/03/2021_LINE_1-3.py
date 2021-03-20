def solution(enter, leave):
    answer = [0] * len(enter)
    idx = 0

    for i in range(len(enter)):
        for x in range(i):
            if enter[x] == leave[idx]:
                enter[x] = 0
                idx += 1

        if i != idx:
            for x in range(i):
                if enter[x] != 0:
                    answer[enter[i]-1] += 1

            for j in range(i):
                if enter[j] != 0:
                    answer[enter[j]-1] += 1

        if enter[i] == leave[idx]:                        
            enter[i] = 0
            idx += 1

    return answer


print(solution([1, 4, 2, 3], [2, 1, 3, 4]))