def solution(table, languages, preference):
    answer = ''
    score = [0] * 5
    idx = 0

    for category in table:
        category_list = category.split()
        tmp_score = 0
        for i in range(1, len(category_list)):
            if category_list[i] in languages:
                tmp_score += (5-i+1) * preference[languages.index(category_list[i])]
        
        if tmp_score > max(score):
            answer = category_list[0]
        elif tmp_score == max(score):
            if ord(answer[0]) > ord(category_list[0][0]):
                answer = category_list[0]
         
        score[idx] = tmp_score
        idx += 1

    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

print(solution(table, languages, preference))