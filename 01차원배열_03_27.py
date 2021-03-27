#1.최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.


n = int(input())

s = list(map(int, input().split()))

print(min(s),max(s))

#2 최대값
d = []
for i in range(9):
    d.append(int(input()))

print(max(d))
print(d.index(max(d))+1)

#3. 숫자의 개수
d= []

for i in range(3):
    d.append(int(input()))

mul = d[0]*d[1]*d[2]
mul = str(mul)

for i in range(10):
    print(mul.count(str(i)))
    
#4나머지


d = []
for i in range (10):
    d.append(int(input())%42)
print(len(set(d)))

#5 평균
#최댓값 M , and 모든 점수를 (점수 / m ) * 100 <- 이렇게 할 때 평균은?
#첫 줄 과목수 n / 둘째는 현재 성적 
import sys

n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
max = max(m)
av = 0 
for i in range(n):
    av += (m[i] / max * 100) / n

print('%.2f'%av)

#6 ox퀴즈
import sys
d=[]

n = int(sys.stdin.readline())
for i in range(n):
    d.append(sys.stdin.readline().rstrip())

for i in d:
    cnt=0
    score=0
    for j in i:
        if j == 'O':
            cnt += 1
            score += cnt
        elif j == 'X':
            score += 0
            cnt = 0
    print(score)

    #6 ox퀴즈
d = []

n = int(input())

for i in range(n):
    d.append(input())

for i in d:
    score = 0
    c = 0
    for j in i:
        if j == 'O':
            c +=1
            score += c
        elif j == 'X':
            c = 0
            score += 0
    print(score)


#7 평균은 넘겠지
import sys

n = int(sys.stdin.readline())
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    student = 0
    average = sum(a[1:]) / a[0]
    for j in a[1:]:
        if j > average:
            student += 1
        else:
            student += 0
    rate = student / a[0] * 100
    print('%.3f'%rate +'%')



