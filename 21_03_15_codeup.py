#6051 : [기초-비교연산] 정수 2개 입력받아 비교하기4(설명)(py)
a , b = map(int, input().split())
if a != b :
    print(True)
else:
    print(False)

#6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기(설명)(py)
#bool( ) 을 이용하면 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력해준다.
a = int(input())

print(bool(a))

# 6053 : [기초-논리연산] 참 거짓 바꾸기(설명)(py)
a = bool(int(input()))

print(not a) #bool은 not and or 사용 가능

# 6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)

a, b = map(int, input().split())
print(bool(a) and bool(b))


if a and b :
    print(bool(1))
else:
    print(bool(0))

    #6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)
a ,b = map(int, input().split())

print(bool(a) or bool(b))

#6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)

a , b = map(int, input().split())

if bool(a) != bool(b):
    print(bool(1))
else:
    print(bool(0))


#6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)

a, b = map(int, input().split())

if a == b:
    print(bool(1))
else:
    print(bool(0))

#6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)

a , b = map(int, input().split())

if a == 0 and b == 0:
    print(bool(1))
else:
    print(bool(0))

#6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기(설명)(py)
#비트연산자(~) not 연산자 = 비트를 1이면 0으로, 0이면 1로 반전시킴. (비트 NOT 연산)
a = int(input())
print(~a)

#비트단위 연산자 공부!

#6060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기(설명)(py)  
# and = & 둘다 1이여야 1이 출력된다
a, b = map(int,input().split())
print(a & b)

#6061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기(설명)(py)
# or = | 이다
a , b = map(int, input().split())

print(a|b)

#6062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기(설명)(py)
#XOR 은 서로 모자란 것만 EX) 1 0 / 0 1 이것은 1로 반환 BUT 1 1 / 0 0 은 0으로 반환
# ^모양으로 승부본다.

a , b = map(int, input().split())
print( a ^ b)

#6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)

a ,b = map(int, input().split())

if a > b:
    print(a)
else:
    print(b)

#정답 
a, b = input().split()
a = int(a)
b = int(b)
c = a if a>=b else b
print(c)


#6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)
# min() 사용 ㅡㅡ;

a , b, c = map(int, input().split())

print(min(a,b,c))


#6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)(py)

a , b, c = map(int, input().split())

if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)


#6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)

a,b,c = map(int,input().split())

if a % 2 == 0:
    print("even")
else:
    print("odd")

if b % 2 == 0:
    print("even")
else:
    print("odd")

if c % 2 == 0:
    print("even")
else:
    print("odd")


    #6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)

a = int(input())
if a < 0:
    if a % 2 == 0:
        print("A")
    else:
        print("B")
else:
    if a % 2 == 0:
        print("C")
    else:
        print("D")

#6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)

a = int(input())
if  a >= 90 :
    print("A")
elif a >= 70:
    print("B")
elif a >= 40:
    print("C")
else:
    print("D")


#6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(py)

a = str(input())

if a == 'A':
    print("best!!!")
elif a == 'B':
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")
    
#6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)

a = int(input())

if 3<= a <=5 :
    print("spring")
elif 6<= a <= 8:
    print("summer")
elif 9 <= a <= 11:
    print("fall")
else:
    print("winter")

if a // 3 == 1:
    print("spring")
elif a // 3 == 2:
    print("summer")
elif a // 3 == 3:
    print("fall")
else:
    print("winter")