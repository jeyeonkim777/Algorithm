# 기존 코딩테스트와 같이 표준 라이브러리(standard library)의 사용은 가능합니다. 단, 그 중 CLI를 구현하기 위한 목적으로 만들어진 표준 라이브러리의 사용은 금지합니다. ex) 사용금지: python의 argparse https://docs.python.org/ko/3/library/argparse.html

def flag_solution(flag_rule, argument): # flag값에 대한 처리해주는 함수
    if flag_rule == 'STRING':
        for arg in argument:
            if 65 <= ord(arg) <= 90 or 97 <= ord(arg) <= 122: # string일때는 영어대소문자만 올 수 있다.
                continue
            else:
                return False

    elif flag_rule == 'NUMBER':
        for arg in argument:
            if 48 <= ord(arg) <= 57: # 숫자일 때는 0 ~ 9 사이의 숫자만 올 수 있다.
                continue
            else:
                print('!!', arg, argument)
                return False
    
    elif flag_rule == 'NULL':
        if argument[0] != '-': # null 일때는 앞에 아무런 argument도 와선 안된다 -> 다른 flag 값이 와야 함
            return False
    
    return True


def arg_solution(argument, flag_rules):
    if argument not in flag_rules:
        return False

    return True


def solution(program, flag_rules, commands):
    answer = []
    flag_rules_dict = {}

    for flag_rule in flag_rules:
        flag_rules_dict[flag_rule.split()[0]] = flag_rule.split()[1]

    for command in commands:
        command_list = command.split()

        if command_list[0] != program: # 입력받은 프로그램으로 시작해아 함, 아닐 시 False append
            answer.append(False)
        
        else:
            result = True
            i = 0
            # for i in range(1, len(command_list)):
            while i <= len(command_list) - 2:
                i += 1
                if command_list[i] in flag_rules_dict:
                    if i == len(command_list) - 1:
                        if flag_rules_dict[command_list[i]] != 'NULL': # 맨 끝에 null값을 제외한 flag 값이 오면 안된다.
                            result = False
                    else:
                        if flag_rules_dict[command_list[i]][-1] == 'S': # 만약 NUMBERS, STRINGS 일 때
                            flag_rules_s = flag_rules_dict[command_list[i]][:-1]
                            idx = 0

                            while True: # 다음값에 flag가 올때까지 돌려주기
                                idx += 1
                                if command_list[i+idx][0] == '-' or i+idx >= len(command_list): # 만약 flag값이 오거나 리스트의 마지막값을 넘으면 루프 빠져나옴
                                    break
                                else:
                                    result = flag_solution(flag_rules_s, command_list[i+idx])

                                if result == False:
                                    break

                            if idx < 2: # 1개의 arguments도 없었을 시 result false로 해줌
                                result = False
                            else:
                                i += idx # loop에서 검사한만큼 idx 뛰어넘기
                        else:
                            result = flag_solution(flag_rules_dict[command_list[i]], command_list[i+1])
                else:
                    result = arg_solution(command_list[i-1], flag_rules_dict)

                if result == False: # 한 번이라도 조건 위배될 시 바로 False 값 append해준 뒤 반복문 break
                    answer.append(result)
                    break

            if result == True: # 모든 조건 만족했을 시 바로 True값 입력
                answer.append(result)
                

    return answer


program = "line"
flag_rules = ["-s STRINGS", "-n NUMBERS", "-e NULL"]
commands = ["line -n 100 102 -s hi -e"]

print(solution(program, flag_rules, commands))