#6089 : [기초-종합] 수 나열하기2(py)
a , r, n = map(int, input().split())

print(a * (r ** (n-1)))

a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(1, n) :
  a = a*r

print(a)

#6090 : [기초-종합] 수 나열하기3(py)
a , m, d, n = map(int, input().split())

for i in range(n-1): # 내가 [0]인덱스를 입력하니까 n-1까지 가야 8을 찎으면 6번까지
    a = a * m + d 


print(a)

#6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)

a , b , c = map(int, input().split())

d = 1

while True:
    if d % a == 0 and d % b == 0 and d % c == 0:
        print(d)
        break
    else:
        d = d+1

#6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []
for i in range(23+1):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1,23+1):
    print(d[i],end=' ')
    

#6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])


for i in range(n-1, -1 , -1):
    print(a[i],end=' ')


    
