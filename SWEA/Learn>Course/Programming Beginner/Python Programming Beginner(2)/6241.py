import sys
sys.stdin = open("ex_050_input.txt")

url_input = input()

protocol, under = url_input.split('://')
host, others = under.split('/')

print(f'protocol: {protocol}')
print(f'host: {host}')
print(f'others: {others}')