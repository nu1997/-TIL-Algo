# 입력없음

ABCD = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
ABCD_list = list(ABCD)
score_list = list(map(lambda x: 4 if x == 'A' else 3 if x == 'B' else 2 if x == 'C' else 1 if x == 'D' else 0, ABCD_list))
score_sum = sum(score_list)

print(score_sum)
