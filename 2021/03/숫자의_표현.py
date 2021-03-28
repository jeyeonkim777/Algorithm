def solution(number):
    answer = 0
    idx = 1
    i = 1
    total = 0
    
    while i <= number:
        total += i
        
        if total == number:
            answer += 1
            i = idx
            idx += 1
            total = 0

        elif total > number:
            while True:
                total -= idx
                if total == number:
                    answer += 1
                    idx += 1
                    break
                elif total < number:
                    break
                idx += 1
            i = idx
            idx += 1
            total = 0
        i += 1
        
    return answer


print(solution(15))