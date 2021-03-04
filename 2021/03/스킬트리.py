def solution(skill, skill_trees):
    arr = [i for i in skill]
    answer = 0

    for skills in skill_trees:
        skill_tmp = list(skill)
        flag = True

        for i in skills:
            if i in skill:
                if i != skill_tmp[0]:
                    flag = False
                    break
                else:
                    skill_tmp.pop(0)
        if flag == True:
            answer += 1

    return answer


    # for i in range(len(skill_trees)):
    #     flag = True
    #     tmp = 0
    #     idx = 0

    #     while tmp != len(skill_trees[i]):

    #         for j in range(idx, len(skill_trees[i])):
    #             if skill_trees[i][j] in skill:
    #                 if skill_trees[i][j] != arr[tmp]:
    #                     flag = False
    #                     break
    #                 else:
    #                     idx = j+1
    #                     break

    #         if flag == False:
    #             break
    #         else:
    #             tmp += 1
                
    #     if flag == True:
    #         answer += 1


# skill = "ABC" 
# skill_trees = ["OPQ"]

skill = "CBDK"
skill_trees = ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]
#  4
#  2
print(solution(skill,skill_trees))