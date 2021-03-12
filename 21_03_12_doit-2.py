#2장. 기본 자료구조와 배열
#예제 2-1

print('학생 그룹 점수의 합계와 평균을 구합니다.')

score1 = int(input('1번 학생의 점수를 입력하세요:'))
score2 = int(input('2번 학생의 점수를 입력하세요:'))
score3 = int(input('3번 학생의 점수를 입력하세요:'))
score4 = int(input('4번 학생의 점수를 입력하세요:'))
score5 = int(input('5번 학생의 점수를 입력하세요:'))

total = 0 
total += score1
total += score2
total += score3
total += score4
total += score5

print("합계는 {}입니다.".format(total))
print("평균은 {}입니다".format(total/5))

#예제 2-2 배열 원소의 최댓값을 구하는 함수 구현
#시퀀스 원소와 최댓값을 출력하기

from typing import Any, Sequence # from 모듈 import 변수 or 함수 내가 사용할 부분만 가져옴

def max_of(a: Sequence) -> Any: #Any 는 제약이 없는 임의 자료형 / sequence는 시퀀스형으로 리스트,바이트 배열, 문자열, 튜플 형, 바이드열 형 이 있다.
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__' :
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.:)'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input("x[{}]값을 입력하셍.:".format(i)))
    print("최대값은 {}입니다.".format(max_of(x)))

#예제 2-3 모듈 테스트하기

from test2 import max_of

print('배열의 최대값을 구합니다')
print('주의,: "End"를 입력하면 종료합니다.')

number = 0
x = [] 

while True:
    s = input("x[{}]값을 입력하세요.:".format(number))
    if s == 'End':
        break
    x.append(int(s))
    number += 1
print("{}개를 입력했습니다.".format(number))
print("최대값은 {}입니다.".format(max_of(x)))

#예제 2-4 배열의 원솟값을 난수로 결정하기
import random
from test2 import max_of

print('난수의 최댓값을 구합니다.')
num = int(input("난수의 개수를 입력하세요.:"))
lo = int(input('난수의 최솟값을 입력하세요.:'))
hi = int(input('난수의 최댓값을 입력하세요.:'))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo,hi)
print("{}".format(x))
print("이 가운데 최댓값은 {} 입니다.".format(max_of(x)))

#예제 2-5 튜플, 문자열,문자열 리스트의 최댓값을 구하기

from test2 import max_of

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS','AAC','FLAC']

print("{}의 최댓값은 {}입니다.".format(t,max_of(t)))
print("{}의 최댓값은 {}입니다.".format(s,max_of(s))) #가장 큰 문자 코드인 t 출력
print("{}의 최댓값은 {}입니다.".format(a,max_of(a))) #사전 순으로 가장큰 FLAC이 출력

#실습 2C-1 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)
x = ['John', 'George', 'Paul', 'Ringo']

for i in range(len(x)):
    print("x[{}] = {}".format(i,x[i]))

    #실습 2C-2 리스트의 모든 원소를 enumerate()함수로 출력
x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x): #변수 2개 받아야 한다
    print("x[{}] = {}".format(i,name))
    #실습 2C-3 리스트의 모든 원소를 enumerate()함수로 스캔하기 (1부터 카운트)

x = ['John', 'George', 'Paul', 'Ringo']

for i,name in enumerate(x, 1): # emurate 는 시작할 숫자 정해주기도 함 1이 시작할 숫자
    print("{}번쨰 = {}".format(i,name))
#실습 2C-4 리스트의 모든 원소를 스캔하기(인덱스 값 넣지 않는다.)

x = ['John', 'George', 'Paul', 'Ringo']

for i in x:
    print(i)

시퀀스(sequence)는 데이터에 순서(번호)를 붙여 나열한 것이다. 
시퀀스의 특징

데이터를 순서대로 하나씩 나열하여 나타낸 데이터 구조다.
특정 위치(~번째)의 데이터를 가리킬 수 있다.

#예제 2-6 배열 원소를 역순으로 정렬

from typing import Any, MutableSequence #MutableSequence 이게 역이고 reversed()랑 같다

def reverse_array(a: MutableSequence) -> None:
    #뮤터블 시퀀스 a의 원소를 역순으로 정렬 
    n = len(a)
    for i in range(n//2): #교환 횟수는 원소 수 // 2 번씩 하면 교환 됨
        a[i] , a[n-i-1] = a[n-i-1], a[i] 

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.:'))
    x = [None] *nx

    for i in range(nx):
        x[i] = int(input("x[{}]값을 입력하시오.".format(i)))
    reverse_array(x)

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print("x[{}] = {}".format(i,x[i]))

        #예제 2-7[A] 기수변화
def card_conv(x:int , r: int) -> str: #x에 들어온 정수를 r진수로 str문자로 바꿔라
    d = ' '
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while x > 0:
        d += dchar[x % r]
        x //=r
    return d[::-1]

if __name__ == "__main__" :
    print('10진수를 n진수로 변환합니다')

    while True:
        while True:
            no = int(input("변환할 값으로 음이 아닌 정수를 입력하시오:")) # 정수
            if no > 0:
                break
        while True:
            cd = int(input('어떤 진수로 변활할까요?:')) #진수
            if 2 <= cd <= 36:
                break
        print("{}진수로는 {}입니다.".format(cd,card_conv(no,cd)))

        retry = input( "한 번 더 변활할까요?(Y ... 예 / N ... 아니오 :")
        if retry in {'N','n'}:
            break

#예제 2c-5 함수 사이에 인수 주고받기
#1부터 n까지 정수의 합 구하기

def sum_1ton(n):
    s = 0
    while n > 0 :
        s += n
        n -= 1
    return s

x = int(input('x값을 입력하시오:'))
print("1부터 {}까지의 정수 합은 {} 입니다.".format(x,sum_1ton(x)))

#예제 2C-6 뮤터블 타입
#리스트에서 임의의 원솟값을 업데이트하기

def change(lst, idx, val):
    lst[idx] = val

x = [ 11, 22, 33, 44, 55 ]
print("x=", x)

index = int(input('업데이트할 인덱스를 선택하세요.:'))
value = int(input("새로운 값을 입력하세요.:"))

change (x, index, value)
print("x={}".format(x))

#예제 2-8 1000이하의 소수를 나열하기

counter = 0 # 나눗셈 횟수 카운트

for i in range(2, 1001):
    for n in range(2, i):
        counter += 1
        if i % n == 0: #소수는 나머지가 0 으로 1과 자기자신의 수로만 나누어 떨어지 는 것
            break
    else:
        print(i)
print("나눗셈을 실행한 횟수 : {}".format(counter))

#예제 2-9 1,000d이하의 소수를 나열하기(알고리즘 개선 1)

counter = 0 
ptr = 0 #이미 찾은 소수의 개수
prime = [None] * 500 #소수 저장 배열

prime[ptr] = 2 #2는 소수이므로 초기 값
ptr += 1

for n in range(3, 1001, 2): #홀수만을 대상 3,5,7,~ 999
    for i in range(1, ptr): # 이미 찾은 소수로 나눔
        counter +=1
        if n % prime[i] == 0: #나누어 떨어지면 소수가 아님
            break
    else: # 끝까지 나누어 떨어지지 않는다면
        prime[ptr] = n # 소수로 배열에 등록
        ptr += 1

for i in range(ptr):
    print(prime[i])
print("나눗셈을 실행한 횟수 : {}".format(counter))
#예제 2-10 # 1000 이하의 소수를 나열하기 (알고리즘 개선2)

counter = 0 
ptr = 0 #이미 찾은 소수의 개수
prime = [None] * 500 #소수 저장 배열

prime[ptr] = 2 #2는 소수이므로 초기 값
ptr += 1

prime[ptr] = 3 #3은 소수
ptr +=1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter +=2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])
print('곱셉과 나눗셈을 실행한 횟수 :{}'.format(counter))
