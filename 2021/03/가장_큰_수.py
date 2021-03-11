def solution(numbers):
    arr = []
    answer = ''
    
    if sum(numbers) == 0:
        return '0'

    for i in numbers:
        str_num = str(i)
        plus_num = str_num
        idx = 0

        while len(plus_num) < 4:
            for i in str_num:
                plus_num += i
                if len(plus_num) == 4:
                    break

        arr.append((plus_num, str_num))

    arr.sort(reverse=True)

    for i in range(len(arr)):
        answer += arr[i][1]

    return answer

print(solution([3, 303, 30]))