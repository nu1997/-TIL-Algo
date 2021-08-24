def solution(sticker):
    answer = 0
    # 고를 수 있는 최대 개수
    l = len(sticker)
    if l < 2:
        return max(sticker)
    n = l // 2
    if l % 2:
        sticker += sticker
        odd = sticker[1::2]
        even = sticker[0::2]
        print(odd, even)
        odd_sum = 0
        even_sum = 0
        for i in range(l - n + 1):
            if odd_sum < sum(odd[i:i+n]):
                odd_sum = sum(odd[i:i+n])
            if even_sum < sum(even[i:i+n]):
                even_sum = sum(even[i:i+n])
        print(odd_sum, even_sum)
        return max(odd_sum, even_sum)
    else:
        odd = 0
        even = 0
        for i in range(len(sticker)):
            if i % 2:
                odd += sticker[i]
            else:
                even += sticker[i]
        return max(odd, even)