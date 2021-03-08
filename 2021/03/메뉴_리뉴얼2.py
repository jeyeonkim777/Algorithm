import itertools

def solution(orders, course):
    answer = []
    for i in range(len(course)):
        order = {}
        for j in range(len(orders)):
            result = itertools.combinations(orders[j], course[i])
            result = list(result)
            for k in range(len(result)):
                result_str = ''.join(sorted(result[k]))
                if result_str in order:
                    order[result_str] += 1
                else:
                    order[result_str] = 1

        order = sorted(order.items(), reverse=True, key=lambda item: item[1])
        for x in range(len(order)):
            if order[0][1] == order[x][1] and order[x][1] > 1:
                answer.append(order[x][0])
            else:
                break
        
    return sorted(answer)
                

print(solution(	["XYZ", "XWY", "WXA"], [2, 3, 4]))