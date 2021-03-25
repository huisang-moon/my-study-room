#1
print("Hello World!")
#2
print("강한친구 대한육군")
print("강한친구 대한육군")

#3고양이 출력
print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

print("""
\    /\\
 )  ( ')
(  /  )
 \(__)|
 """)

 #4 개 출력 # \\ 이거 잘 확인
print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')

#5~8. A+B , - , * , / 
a , b = map(int, input().split())

print(a + b)


#9. A+B, A-B, A*B, A/B(몫), A%B(나머지) 사칙연산
a , b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

#10. (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
#    (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
A , B, C = map(int, input().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

#11 3자리수 x 3자리수
# 인덱스 사용하려면 문자열로 사용해야함!! 이걸 놓쳤다.
a = int(input())
b = input()

print(a*int(b[2])) 
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))