def solution(N):
    answer = 0
    
    while True:
        if N == 1:
            return answer + 1
        
        if N % 2 == 1:
            N -= 1
            answer += 1
        
        N = N//2