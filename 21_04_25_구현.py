#1 ACM 호텔

t = int(input())
for i in range(t):
    h , w , n = map(int,input().split())
    floor = n % h
    방번호 = n // h + 1
    if n % h == 0 :
        floor = h 
        방번호 = n // h
    print(floor * 100 + 방번호)

for i in range(int(input())):
    h, w, n = map(int,input().split())
    floor = n % h 
    room = n // h + 1
    if n % h == 0 :
        floor = h 
        room = n // h 
    print(floor * 100 + room)

#2 분수찾기

n = int(input())
line = 1

while n > line:
    n -= line
    line += 1
if line % 2 == 0:
    top = n 
    bottom = line - n + 1 # 분자 + 분모 = line + 1
else :
    top = line - n + 1
    bottom = n
print(top,"/",bottom,sep="")

num = int(input())
line = 1 

while num > line:
    num -= line
    line += 1 
if line % 2 == 0 :
    top = num
    bottom = line + 1 - num 
else:
    top = line + 1 - num
    bottom = num 
print(top,bottom,sep="/")

#3별찍기 -9
num = int(input())

for i in range(num,0,-1):
    print(" " * (num-i) + "*" * (2*i-1))
for i in range(2,num+1):
    print(" " * (num-i)+ "*" * (2*i-1))

    #4 덩치
num = int(input())
arr = []

for i in range(num):
    w , h = map(int,input().split())
    arr.append((w,h))

for i in range(num):
    rank = 1
    for j in range(num):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1] :
            rank += 1
    print(rank,end=" ")

num = int(input())

arr = [] 

for i in range(num):
    w , h = map(int, input().split())
    arr.append((w,h))

#비교
for i in range(num):
    rank = 1
    for j in range(num):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    print(rank,end=" ")

#5 별찍기 - 5
n = int(input())

for i in range(1,n+1):
    print(" "* (n-i) + "*" * (2 * i - 1))

#6 피보나치 수
a = int(input())


def fib_3(n):
    a , b = 1, 1
    for i in range(n):
        yield a
        a ,b = b, a + b

for i in fib_3(a):
    c = i
print(c)