def solution(citations):
    citations.sort()
    answer = 0

    for i in range(len(citations)):
        if citations[i] > len(citations) - i:
            if len(citations) - i > answer:
                answer = len(citations) - i
    
    return answer


print(solution([12, 11, 10, 9, 8, 1]))