def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        check_stack = ''
        flag = 1
        for s in skill_tree:
            if s in skill:
                check_stack += s
                if skill.index(s) != check_stack.index(s):
                    flag = 0
                    break
        if flag == 1:
            answer += 1
    return answer