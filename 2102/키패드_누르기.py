import sys

패드 누르기 
def Length(leftHand, rightHand, arr, hand):
​
    ltmp = abs(leftHand[0] - arr[0]) + abs(leftHand[1] - arr[1])
    rtmp = abs(rightHand[0] - arr[0]) + abs(rightHand[1] - arr[1])
​
    if ltmp > rtmp:
        return 'R'
​
    elif ltmp < rtmp:
        return 'L'
    
    else:
        if hand == 'right':
            return 'R'
        else:
            return 'L'
    
​
def solution(numbers, hand):
    leftHand = [3, 0]
    rightHand = [3, 2]
    
    answer = []
​
    for num in numbers:
        rtmp = 0
        ltmp = 0
        
        if num in [1, 4, 7]:
            leftHand = [((num+2)//3)-1, 0]
            answer.append('L')
​
        elif num in [3, 6, 9]:
            rightHand = [(num//3)-1, 2]
            answer.append('R')
​
        else:
            tmp = []
            if num == 2:
                tmp = Length(leftHand, rightHand, [0, 1], hand)
                if tmp == 'R':
                    answer.append(tmp)
                    rightHand = [0, 1]
                else:
                    answer.append(tmp)
                    leftHand = [0, 1]
            elif num == 5:
                tmp = Length(leftHand, rightHand, [1, 1], hand)
                if tmp == 'R':
                    answer.append(tmp)
                    rightHand = [1, 1]
                else:
                    answer.append(tmp)
                    leftHand = [1, 1]
            elif num == 8:
                tmp = Length(leftHand, rightHand, [2, 1], hand)
                if tmp == 'R':
                    answer.append(tmp)
                    rightHand = [2, 1]
                else:
                    answer.append(tmp)
                    leftHand = [2, 1]
            else:
                tmp = Length(leftHand, rightHand, [3, 1], hand)
                if tmp == 'R':
                    answer.append(tmp)
                    rightHand = [3, 1]
                else:
                    answer.append(tmp)
                    leftHand = [3, 1]
​
​
    return ''.join(answer) 

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"


print(solution(numbers, hand))