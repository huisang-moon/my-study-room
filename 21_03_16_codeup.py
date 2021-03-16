#6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기(설명)(py)

n = 1 #처음 조건 검사를 통과하기 위해 0 아닌 값을 임의로 저장
while n != 0:
    n = int(input())
    if n !=0:
        print(n)


#6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1(설명)(py)

n = int(input())

while n != 0:
    print(n)
    n = n-1

    #6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(py)
# 입력 5 출력 4 3 2 1 0
n = int(input())

while n != 0:
    print(n-1)
    n = n-1

#6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)
a = ord(input()) #문자를 받을거야 그리고 ord()로 아스키코드 값으로 바꾼다
b = ord('a') # 알파벳 a의 정수값

while b<=a:
    print(chr(b),end=' ') # chr() 아스키 코드 값 -> 문자로 변환하는 함수
    b += 1

#6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1(py)
#입력이 4 출력 0 1 2 3 4 (줄 바꿔가며)

a = int(input())
n = 0

if a != 0:
    while n != a+1: #n이랑 a+1이랑 같아지는 순간 빠져 나온데이~
        print(n)
        n += 1
else:
    print(n)

#6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2(설명)(py)

a = int(input())

for i in range(a+1):
    print(i)

#6077 : [기초-종합] 짝수 합 구하기(설명)(py)

a = int(input())
b = 0



while a != 0 :
    if a % 2 != 0:
        a -=1
    else:
        b += a
        a -= 1

print(b)

#6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기(py)

a = str(input())

while a != "q":
    print(a)
    a = str(input())
    if a == "q":
        print(a)
        break

#6079 : [기초-종합] 언제까지 더해야 할까?(py)

a = int(input())
b = 0
for i in range(1,a+1):
    b = b + i 
    if b >= a:
        print(i)
        break

#6080 : [기초-종합] 주사위 2개 던지기(설명)(py)

a , b = map(int, input().split())


for i in range(1,a+1):
    for j in range(1,b+1):
        print(i,j)

#6081 : [기초-종합] 16진수 구구단 출력하기(py)

a = input()
b = int(a,16) # 16진수
for i in range(1, 16):
    c = int(b * i)
    print('%s*%X=%X'%(a,i,c))# '문자열 곱하기 16진수 = 16진수'%(어디어디 들어가나)

    
    
    
 n = int(input(), 16)

for i in range(1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
  
'''
또는
print("%X*%X=%X"%(n,i,n*i))

'''

문자열 포맷 코드
문자열 포매팅 예제에서는 대입해 넣는 자료형으로 정수와 문자열을 사용했으나 이 외에도 다양한 것을 대입할 수 있다. 문자열 포맷 코드로는 다음과 같은 것이 있다.

코드	설명
%s	문자열(String)
%c	문자 1개(character)
%d	정수(Integer)
%f	부동소수(floating-point)
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)

    
#6082 : [기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)

a = int(input())

for i in range(1, a+1):
    if i % 10 == 3 :
        print("X",end=' ')
    elif i % 10 == 6:
        print("X",end=' ')
    elif i % 10 == 9:
        print("X",end=' ')
    else:
        print(i, end=' ')


n = int(input())

for i in range(1, n+1) :
  if i%10==3 or i%10==6 or i%10==9 : # or 역을때 산수식도 같이 넣어주기
    print("X", end=' ')
  else :
    print(i, end=' ')
    

    #6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)

a, b, c = map(int, input().split())

for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k)

print(a * b* c)

#6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)
h , b, c , s = map(int,input().split())
sum = ( h * b * c * s ) / 8 # 비트 -> 바이트로 고친것
sum = sum / (2**20) # 1키로바이트는 1024바이트 / 1메가바이트는 1024 키로바이트
print("%.1f MB"%(sum))


h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

print(round(h*b*c*s/8/1024/1024, 1), "MB") #round() 는 반올림 함수이다