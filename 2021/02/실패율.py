import sys

def solution(N, stages):

    stages.sort()
    people = len(stages)
    obj = {}
    answer = []
    tmp = 0

    for i in range(1, N+1):

        if people == 0:
            obj[i] = 0

        else:
            num = 0
            
            while tmp < len(stages):
                if stages[tmp] == i:
                    num += 1
                    tmp += 1
                else:
                    break

            obj[i] = num/people

            people -= num

    answer_tuple = sorted(obj.items(), key = lambda obj: obj[1], reverse = True)

    for i in range(len(answer_tuple)):
        answer.append(answer_tuple[i][0])

    return answer


N = 4
stages = [1, 1, 1, 1, 1]

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))

    