import sys
sys.stdin = open("ex_031_input.txt")

def palindromeCheck(m_str):
   #문자 길이만큼 반복
   for i in range(0, len(m_str)):
      #앞과 뒤를 비교하며 틀리다면 False를 리턴하고 모두통과라면 True 리턴
      if m_str[i] != m_str[len(m_str)-1-i]:
         return False
      return True
 
t = input()
print(t)
if palindromeCheck(t) : 
   print("입력하신 단어는 회문(Palindrome)입니다.")
else :
   print("입력하신 단어는 회문(Palindrome)이 아닙니다.")
