template = {'-', '_', '.'}

def solution(new_id):
    lowered = new_id.lower()
    removed = ''
    for char in lowered:
        try:
            if char.isalpha() or char.isdigit() or char in template:
                # + step 3
                if char == '.' and removed[-1] == '.':
                    pass
                else:
                    removed += char
        except:
            continue
    removed = removed.lstrip('.').rstrip('.')
    if removed == '':
        return 'aaa'
    if len(removed) >= 16:
        return removed[:15].rstrip('.')
    elif len(removed) <= 2:
        result = removed
        while len(result) < 3:
            result += removed[-1]
        return result
    else:
        return removed

### 다른 사람의 풀이 BEST 1 ###
################ 정규식 #####

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

### 다른 사람의 풀이 BEST 2 ###
################ 함수화 #####

# def solution(new_id):
#     id = step1(new_id)
#     id = step2(id)
#     id = step3(id)
#     id = step4(id)
#     id = step5(id)
#     id = step6(id)
#     id = step7(id)
#     return id