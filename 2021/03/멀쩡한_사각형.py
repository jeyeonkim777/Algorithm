from math import gcd

def solution(w,h):

    if w == h:
        return w * h - h

    if gcd(w, h) == 1:
        return w * h - (w + h - 1)
    else:
        num = gcd(w, h)
        answer = gcd(w, h)
        while True:
            tmp = gcd(w//num, h//num)

            if tmp == 1:
                print(num)
                return w * h - (answer * ((w//num) + (h//num) - 1))
            else:
                answer *= num
                num = tmp

            


print(solution(8, 12))