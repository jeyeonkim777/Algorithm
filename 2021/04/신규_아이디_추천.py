def solution(new_id):
    new_id = new_id.lower()

    for i in new_id:
        if i in '~!@#$%^&*()=+[{]}:?,<>/':
            new_id = new_id.replace(i,'')

    new_id = list(new_id)

    for i in range(len(new_id)-1):
        if new_id[i] == '.' and new_id[i+1] == '.':
            new_id[i] = ''

    new_id = ''.join(new_id)
    
    if len(new_id) == 0:
        return 'aaa'
    else:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if len(new_id) == 0:
            new_id += 'a'
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            return new_id[:-1]

    while len(new_id) < 3:
        new_id += new_id[-1]
        
    return new_id


print(solution("abcdefghijklmn..p"))