def backtrack(menus, r, visit, order, course):
    flag = True
    for x in range(len(course) - 1):
        if course[x] > course[x+1]:
            flag = False
            break
    if flag == False:
        return
    if len(course) == r:
        course_str = ''.join(sorted(course))
        if course_str in order:
            order[course_str] += 1
        else:
            order[course_str] = 1
    else:
        for menu in range(len(menus)):
            if visit[menu]:
                continue
            visit[menu] = 1
            course.append(menus[menu])
            backtrack(menus, r, visit, order, course)
            visit[menu] = 0
            course.pop()

    return order


def solution(orders, course):
    answer = []

    for i in range(len(course)):
        order = {}
        for j in range(len(orders)):
            visit = [0] * len(orders[j])
            arr = []
            backtrack(orders[j], course[i], visit, order, arr)

        order = sorted(order.items(), reverse=True, key=lambda item: item[1])
        
        for i in range(len(order)):
            if order[0][1] == order[i][1] and order[i][1] > 1:
                answer.append(order[i][0])
            else:
                break
        
    return sorted(answer)


print(solution(	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))