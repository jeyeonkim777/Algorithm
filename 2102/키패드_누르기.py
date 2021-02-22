import sys

def Length(leftHand, rightHand, leftNum, rightNum, arr, hand):

    ltmp = abs(leftHand[0] - arr[0]) + abs(leftHand[1] - arr[1])
    rtmp = abs(rightHand[0] - arr[0]) + abs(rightHand[1] - arr[1])

    if ltmp > rtmp:
        return 'R'

    elif ltmp < rtmp:
        return 'L'
    
    else:
        if hand == 'right':
            return 'R'
        else:
            return 'L'
    

def solution(numbers, hand):
    leftHand = [3, 0]
    leftNum = 10

    rightHand = [3, 2]
    rightNum = 12
    
    answer = []

    for num in numbers:
        rtmp = 0
        ltmp = 0
        
        if num in [1, 4, 7]:
            leftNum = num
            leftHand = [((num+2)//3)-1, 0]
            answer.append('L')

        elif num in [3, 6, 9]:
            rightNum = num
            rightHand = [(num//3)-1, 2]
            answer.append('R')

        else:
            tmp = []
            if num == 2:
                tmp = Length(leftHand, rightHand, leftNum, rightNum, [0, 1], hand)
                if tmp == 'R':
                    rightNum = 2
                    answer.append(tmp)
                    rightHand = [0, 1]
                else:
                    leftNum = 2
                    answer.append(tmp)
                    leftHand = [0, 1]
            elif num == 5:
                tmp = Length(leftHand, rightHand, leftNum, rightNum, [1, 1], hand)
                if tmp == 'R':
                    rightNum = 5
                    answer.append(tmp)
                    rightHand = [1, 1]
                else:
                    leftNum = 5
                    answer.append(tmp)
                    leftHand = [1, 1]
            elif num == 8:
                tmp = Length(leftHand, rightHand, leftNum, rightNum, [2, 1], hand)
                if tmp == 'R':
                    rightNum = 8
                    answer.append(tmp)
                    rightHand = [2, 1]
                else:
                    leftNum = 8
                    answer.append(tmp)
                    leftHand = [2, 1]
            else:
                tmp = Length(leftHand, rightHand, leftNum, rightNum, [3, 1], hand)
                if tmp == 'R':
                    rightNum = 0
                    answer.append(tmp)
                    rightHand = [3, 1]
                else:
                    leftNum = 0
                    answer.append(tmp)
                    leftHand = [3, 1]


    return ''.join(answer)        

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"


print(solution(numbers, hand))