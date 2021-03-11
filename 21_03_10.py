#세 정수의 최댓값 구하기

def max(a, b, c) : 
    max = a
    if b > max :
        max = b
    if c > max :
        max = c
    return max

print(max(3,222,555) )
#return 값이 필요하다 반환이 없으니

def med3(a,b,c):
    if a >=b :
        if b>=c:
            return b
        elif a <=c :
            return a
        else:
            return c
    elif a > c:
        return a
    else:
        return b
print('세 정수의 중앙값을 구합니다.')
a = int(input("a값 :"))
b = int(input("b값 :"))
c = int(input("c값 :"))

print(f"중앙값은 {med3(a,b,c)} 입니다") # 포매팅 개념!

def med3(a,b,c):
    if ( b>=a and c<=a ) or ( b<=a and c>=a):
        return a
    elif (a > b and c < b ) or ( a < b and c > b):
        return b
    else :
        return c
print('세 정수의 중앙값을 구합니다.')
a = int(input("a값 :"))
b = int(input("b값 :"))
c = int(input("c값 :"))

print(f"중앙값은 {med3(a,b,c)}")