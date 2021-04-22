#세 수

a, b, c = map(int,input().split())

if a > b > c or c > b > a:
    print(b)
elif a > c > b or b > c > a :
    print(c)
elif b > a > c or c > a > b :
    print(a) 
elif a == b == c:
    print(a)
elif a == b > c or a == b < c :
    print(a)
elif b == c > a or b == c < a:
    print(b)
elif a == c > b or a == c < b:
    print(c)  

#아스키코드

n = input()
print(ord(n))

# A+B - 2
a = int(input())
b = int(input())
print(a+b)

#별찍기 -3 
n = int(input())
for i in range(n,0,-1):
    print('*' * i) 

#단어의 개수

n = input().split()
array = list(n)
print(len(array))

#알파벳 찾기 
s = list(map(str, input()))
alpha = list("abcdefghijklmnopqrstuvwxyz")
array = [-1 for i in range(len(alpha))]
for i in range(len(s)):
    if array[alpha.index(s[i])] == -1:
        array[alpha.index(s[i])] = i
for j in array:
    print(j , end=' ')

#별찍기 - 4
n = int(input())
space = 0
for i in range(n,0,-1):

    if n == i :
        print('*' * i)
    else:
        print(' ' * space, '*' * i )
        space += 1 

#별찍기 - 4
n = int(input())
for i in range(1,n+1):
    print(" " * (i-1) + "*" * (n-i+1))