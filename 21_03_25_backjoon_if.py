#1 두 수 비교하기
#A가 B보다 큰 경우에는 '>'를 출력한다.
#A가 B보다 작은 경우에는 '<'를 출력한다.
#A와 B가 같은 경우에는 '=='를 출력한다.

a , b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

#2시험 성적
#90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F

a = int(input())

if  a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
elif a >= 60:
    print('D')
else:
    print('F')

#3 윤년
#연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램
#윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 윤년 % 4 == 0 and 윤년 % 100 != 0 (앞은 한 세트 ) or 윤년 % 400 == 0 (얘는 독립)

a = int(input())

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('1')
else:
    print('0')
    
#4. 사분면 고르기
#1사분면 (++) 2사분면 (-+) 3사분면 (--) 4사분면 (+-) a = x / b = y
x = int(input()) #x
y = int(input()) #y

if x>0 and y >0 :
    print('1')
elif x <0 and y < 0:
    print('3')
elif x > 0 and y < 0: #+ - 
    print('4')
else:
    print('2')


#5 알람시계
# "45분 일찍 알람 설정하기" 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다.
#현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 
# 이를 언제로 고쳐야 하는지?
#24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 

h,m = map(int, input().split())

if m - 45 < 0:
    if h == 0:
        h = 23
    else:
        h -= 1
    m = (60-45) + m 

else:
    m = m - 45

print(h,m)

