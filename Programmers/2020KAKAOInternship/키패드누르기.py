position_dict = {
    # 1 2 3
    '1': (-1, -1), '2': (0, -1), '3': (1, -1),
    # 4 5 6
    '4': (-1, 0), '5': (0, 0), '6': (1, 0), 
    # 7 8 9
    '7': (-1, 1), '8': (0, 1), '9': (1, 1),
    # * 0 #
    '*': (-1, 2), '0': (0, 2), '#': (1, 2)
}


def solution(numbers, hand):
    answer = ''
    left_hand = '*'
    right_hand = '#'
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left_hand = num
        elif num in [3, 6, 9]:
            answer += "R"
            right_hand = num
        else:
            strnum = str(num)
            str_lh = str(left_hand)
            str_rh = str(right_hand)

            left_distance = (
                abs(position_dict[strnum][0] - position_dict[str_lh][0])
                + 
                abs(position_dict[strnum][1] - position_dict[str_lh][1])
            )
            right_distance = (
                abs(position_dict[strnum][0] - position_dict[str_rh][0])
                + 
                abs(position_dict[strnum][1] - position_dict[str_rh][1])
            )
            
            if left_distance > right_distance:
                answer += 'R'
                right_hand = int(strnum)
            elif left_distance < right_distance:
                answer += 'L'
                left_hand = int(strnum)
            else:
                if hand == 'right':
                    answer += 'R' 
                    right_hand = int(strnum)
                else:
                    answer += 'L'
                    left_hand = int(strnum)
    return answer

'''
유클리드 거리와 맨하탄 거리
유클리드 거리 => 왼손 : (11)+(11), 오른손 : (00)+(22) (다름)
맨하탄 거리 => 왼손 : 1+1, 오른손 : 0+2; (같음)
'''