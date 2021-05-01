#1 피보나치 수
#재귀는 시간초과
def fibonacci(a):
    if a == 1 or a == 2 :
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)

n = int(input())
print(fibonacci(n))

#일반 식(pass)
def fibonacci(n):
    a , b = 1 , 1
    if n ==1 or n == 2:
        return 1
    for i in range(1,n):
        a , b = b , a + b
    return a
n = int(input())
print(fibonacci(n))

#2 별찍기 - 13
n = int(input())

for i in range(1,n+1):
    print("*"*i)
for j in range(n-1,0,-1):
    print("*"*j)

#3 별찍기 - 8
n = int(input())

for i in range(1,n+1):
    print("*"* i + " "*(n-i) + " " *(n-i) + "*"*i)
for j in range(n-1,0,-1):
    print("*"*j + " " * (n-j)+" " * (n-j) + "*" * j)

#3 별찍기 - 7
n = int(input())

for i in range(1,n+1):
    print(" "*(n-i) + "*" * (2*i-1))
for j in range(n-1,0,-1):
    print(" " * (n-j) + "*" * (2*j-1))
    

