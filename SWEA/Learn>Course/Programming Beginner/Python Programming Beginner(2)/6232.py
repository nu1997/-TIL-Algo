import sys
sys.stdin = open("ex_030_input.txt")

x = input()


if x == x[::-1]:
    print(x)
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print(x)
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")