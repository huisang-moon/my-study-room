#1-2 반복하는 알고리즘 
#예제 1-7
#1부터 n까지 정수의 합 구하기1(while 사용)

print('1부터 n까지 정수의 합을 구합니다')
n = int(input("n값을 입력:"))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("1부터 {}까지 정수의 합은 {} 입니다.".format(n,sum))

#1-8 for 반복문

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input("n값을 입력하시요:"))

sum = 0 
for i in range(1, n+1):
    sum += i
print("1부터 {}까지의 합은 {} 입니다.".format(n,sum))

#1-9 오름차순

print('a부터 b까지의 정수의 합을 구합니다.')
a = int(input('정수 a 입력하시오:'))
b = int(input('정수 b 입력하시오:'))

if a > b:
    a,b = b,a #교환 오름차순 기준 

sum = 0
for i in range(a,b+1):
    sum += i
print("{}부터 {}까지의 정수의 합은 {} 입니다.".format(a,b,sum))
##1-10 반복 과정에서 조건 판단하기 (1)

print('a부터 b까지의 정수의 합을 구합니다.')
a = int(input('정수 a 입력하시오:'))
b = int(input('정수 b 입력하시오:'))

if a > b:
    a,b = b,a #교환 오름차순 기준 

sum = 0
for i in range(a,b+1):
    if i < b :
        print("{} +".format(i),end=" ")
    else:
        print("{} =".format(i),end=" ")
    sum += i 
print(sum)

#1-11 (1-10)을 개선함

print('a부터 b까지의 정수의 합을 구합니다.')
a = int(input('정수 a 입력하시오:'))
b = int(input('정수 b 입력하시오:'))

if a > b:
    a,b = b,a #교환 오름차순 기준 

sum = 0
for i in range(a,b):
    print("{} +".format(i),end='')
    sum +=i 
print("{} =".format(b), end="")
sum += b
#1-12 반복 과정에서 조건 판단하기 2
print('+와 -를 번갈아 출력합니다.')
n = int(input("몇 개를 출력할까?"))

for i in range(n):
    if i % 2 : #나머지 연산자
        print("-", end="") #홀수 -
    else:
        print("+", end="") # 짝수 +
print()
#1-13 
print('+와 -를 번갈아 출력합니다.')
n = int(input("몇 개를 출력할까?"))

for i in range(n//2):
    print('+-', end="")
if n % 2 :
    print('+', end="")
print()
#1-14 반복 과정에서 조건 판단하기 (3)
print("*을 출력합니다.")
n = int(input("몇 개를 출력할까요?"))
m = int(input("몇 개마다 줄바꿈할까요?"))

for i in range(n):
    print("*",end="")
    if i % m == m-1 :
        print()
if n % m :
    print()

#1-15 반복 과정에서 조건 판단하기 (3) 개선

print("*을 출력합니다.")
n = int(input("몇 개를 출력할까요?"))
m = int(input("몇 개마다 줄바꿈할까요?"))
#1-16 양수만 입력받기
print("1부터 n까지 정수의 합을 구합시다.")

while True:
    n = int(input("n값을 입력하세요.:"))
    if n > 0 :
        break
sum = 0 
i = 1

for i in range(1, n+1):
    sum += i
    i += 1

print("1부터 {}까지 정수의 합은 {}입니다.".format(n,sum))

#1-17 직사각형 넓이로 변의 길이 구하기!

area = int(input("직사각형의 넓이를 입력하세요.:"))

for i in range(1, area + 1):
    if i * i > area :
        break
    if area % i:
        continue
    print("{} x {}".format(i,area//i))

#1-18 else문이 뒤따르는 for문을 구현하는 프로그램!

import random

n = int(input('난수의 개수를 입력하시오.:'))

for i in range(n):
    r = random.randint(1,45)
    print(r,end=' ')
    if r == 5:
        print("\n 프로그램을 종료합니다.")
        break
else:
    print("\n난수 생성을 종료합니다.")

for i in range(n//m):
    print("*" * m)
rest = n % m
if rest:
    print("*" * rest)

1-19 반복문 건너뛰기와 여러 범위 스캔하기

for i in range(1, 13):
    if i == 8 :
        continue
    print(i, end=" ")

#드모드간의 법칙

print("2자리 양수를 입력하시오:")

while True:
    no = int(input("값을 입력:"))
    if no >= 10 and no <=99 :
        break
print("입력받은 양수는 {}입니다.".format(no))

#1-21 구구단의 곱셈 출력하기

print("-" * 27)
for i in range(1,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print()
print("-" * 27)
#1-22 직각 이등변 삼각형으로 출력

print("왼쪽 아래가 직각인 이등변 삼각형을 출력!")
n = int(input("짧은 변의 길이를 입력하세요:"))

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
#1-23 오른쪽 아래가 직각인 이등변 삼각형

print("오른쪾 아래가 직각인 이등변 삼각형을 출력합니다.")
n = int(input("짧은 변의 길이를 입력하세요:"))

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()


