def solution(people, limit):
    answer = 0
    people.sort()

    idx_front = 0
    idx_back = len(people) - 1

    while idx_front < idx_back:

        if people[idx_front] + people[idx_back] <= limit:
            idx_front += 1
            idx_back -= 1
        else:
            idx_back -= 1
            
            
        answer += 1
        # print(idx_front, idx_back)

        if idx_front == idx_back:
            answer += 1
            break

    return answer





people = [70, 50, 80]
limit = 100

print(solution(people, limit))