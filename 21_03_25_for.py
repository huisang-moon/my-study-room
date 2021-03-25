#1. 구구단

n = int(input())

for i in range(1,9+1):
    print(f'{n} * {i} = {n*i}')

    #2. A+B-3

n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    print(a+b)

#3 합
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
add = 0

for i in range(n+1):
    add += i 

print(add)

#4 빠른 A+B sys.stdin.readline <- import 뺴고 input()이랑 똑같음.
import sys

n = int(sys.stdin.readline())

for i in range(n):
    a , b = map(int, sys.stdin.readline().split())
    print(a + b)

#5.N 찍기
import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):
    print(i)

#6. 기찍 N

import sys

n = int(sys.stdin.readline())

for i in range(n,0,-1):
    print(i)

#7. a+b-7
import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):
    a,b = map(int,sys.stdin.readline().split())
    print(f"Case #{i}: {a+b}")
    
#8. a+b-8

import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):
    a,b = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")

    #9. 별찍기-1

n = int(input())

for i in range(1,n+1):
    print("*" * i)

#10. 별찍기-2
import sys

n = int(sys.stdin.readline())
j = 1
for i in range(n-1,-1,-1):   
    print(' '* i + '*' * j)
    j += 1

#11. X보다 작은 수
#정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램

import sys

n , x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if a[i] < x:
        print(f'{a[i]}',end=' ')
