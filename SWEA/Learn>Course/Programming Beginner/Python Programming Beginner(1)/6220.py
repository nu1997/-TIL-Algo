import sys
sys.stdin = open("ex_020_input.txt")

a = input()
if 'a' <= a <= 'z':
    print("%s 는 소문자 입니다." % (a))
elif 'A' <= a <= 'Z':
    print("%s 는 대문자 입니다." % (a))