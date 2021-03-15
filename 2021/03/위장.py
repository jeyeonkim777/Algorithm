def solution(clothes):
    answer = 1
    obj = {}
    arr = []
    cnt = 1

    for cloth in clothes:
        if cloth[1] in obj:
            obj[cloth[1]] += 1
        else:
            obj[cloth[1]] = 1

    for value in obj.values():
        answer *= (value + 1)

    return answer -1

clothes = [
["a","aa"],
["b","aa"],
["c","aa"],
["aa","bb"],
["bb","bb"],
["c_c","bb"],
["aaa","cc"],
["bbb","cc"],
["ccc","cc"]
]
print(solution(clothes))