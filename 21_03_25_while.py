#1. A+B - 5 

import sys


while True:
    a , b = map(int, sys.stdin.readline().split())   
    if a == 0 and b == 0:
        break
    else:
        print(a+b)

#2.A+B - 4 


while True:
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:
        break

#더하기 사이클

n = int(input())
num = n
cnt = 0

while True:
    a = num // 10 # 10자리
    b = num % 10  # 1의 자리
    c = (a+b) % 10 #합의 1의자리 쓰겠다
    num = (b * 10) + c 
    cnt += 1
    if num == n:
        break

print(cnt)
