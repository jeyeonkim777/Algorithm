def solution(progresses, speeds):

    tmp = 0
    count = 0
    answer = []
    num = len(speeds)

    while tmp < num:

        for i in range(tmp, num):
            progresses[i] += speeds[i]

        if progresses[tmp] >= 100:

            while progresses[tmp] >= 100:
                count += 1
                tmp += 1

                if tmp >= num:
                    break

            answer.append(count)
            count = 0

    return answer
            

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))