import math
def solution(n, words):
    answer = [0, 0]
    obj = {}
    previous = words[0][0]

    for i in range(len(words)):
        if words[i] in obj or previous != words[i][0]:
            print(i)
            answer[1] = math.ceil((i+1) / n)
            answer[0] = (i+1) - (answer[1] - 1) * n
            return answer
        else:
            obj[words[i]] = 1
            previous = words[i][-1]

    return answer
n = 3
words =	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print(solution(n, words))