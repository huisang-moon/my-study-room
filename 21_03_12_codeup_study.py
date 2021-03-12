#6033. 아스키코드로 변화주는게 포인트
# ord() 함수 : 특정문자 -> 아스키 코드
# chr()함수 : 아스키 코드 -) 문자로
a = input()
b = ord(a) 
print(chr(b+1)) 

#6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기(설명)(py)
a, b = input().split(' ')
c = int(a) - int(b)
print(c)

#6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기(설명)(py)
a, b = input().split(" ")
a = float(a)
b = float(b)
print(a * b)

#6036 : [기초-산술연산] 단어 여러 번 출력하기(설명)(py)
a , b = input().split()
print(a * int(b))

#6037 : [기초-산술연산] 문장 여러 번 출력하기(설명)(py)
a = input()
b = input()
print(int(a)* b)

#6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기(설명)(py)
a , b = input().split()
print(int(a)**int(b))

#6039 : [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기(py)
a , b = input().split()
print(float(a)**float(b))

#6040 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기(설명)(py)

a , b = input().split()
print(int(a)//int(b))

#6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기(설명)(py)
a , b = input().split()
print(int(a)%int(b))

#6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기(설명)(py)
#round(a,b) b는 (소숫점 자리수) 이 round로 처리된 값을 
# print로 출력하는 경우 소숫점 둘째자리 이상 불필요한 0이 있는 경우 출력되지 않는다.
a = input()
a = float(a)
print(round(a,2))

#6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)
a, b = input().split()
a = float(a)
b = float(b)
c = a/b 
print('%.3f'%c) # '%.원하는 자리수f<실수'%변수

#6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)
a, b = input().split()
a = int(a)
b = int(b)
c = a / b
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print('%.2f'%c)

#6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)

#map 함수 사용 a,b,c = map(int,input().split())

a, b, c = map(int,input().split())
add = a + b + c 
print(add,'%.2f'%(add/3))


#a, b, c = input().split()
#a = int(a)
#b = int(b)
#c = int(c)
#add = a + b + c
#avr = add / 3
#print(add,'%.2f'%avr)

#6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기(설명)(py)
a = int(input())
print(2 *a)
#정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>를 이용할 수 있다.

#6047 : [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기(설명)(py)
#n << m : n * 2의 m승
#n >> m : n / 2의 m승
#예를 들어 1 3 이 입력되면 1을 2**3(8)배 하여 출력한다.

a , b = map(int,input().split())
print(a<<b)

print(a * 2**b)


#6048 : [기초-비교연산] 정수 2개 입력받아 비교하기1(설명)(py)
a , b =map(int,input().split())
if a < b:
    print(True) # 0이면 false가 나오고 1이면 true가 나오자나
else:
    print(False)

#6049 : [기초-비교연산] 정수 2개 입력받아 비교하기2(설명)(py)
a , b = map(int,input().split())
print(a == b)

#6050 : [기초-비교연산] 정수 2개 입력받아 비교하기3(설명)(py)
a, b = map(int,input().split())
print(b>=a)
