def solution(brown, yellow):
    answer = []
    total = brown + yellow

    for i in range(1, total):
        if total % i == 0:
            if (total // i) - 2 > 0 and i - 2 > 0:
                print((total // i) - 2, i - 2, i)
                if ((total // i) - 2) * (i - 2) == yellow:
                    answer.append(i)
                    answer.append(total // i)
                    break

    return sorted(answer, reverse=True)


print(solution(10, 2))