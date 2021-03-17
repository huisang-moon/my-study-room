# 6085 : [기초-종합] 그림 파일 저장용량 계산하기(py)

w, h , b = map(int, input().split())

a = (w * h * b) / 8 / 2**20

print(round(a,2),"MB")


#6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)
# input 10 ->output 1+2+3+4+5 = 15가 출력
a = int(input())
b = 0

for i in range(1,a+1):
    b +=i
    if b>=a:
        break

print(b)

a=int(input())
s=0
c=0

while True:
    s=s+c
    c=c+1
    if s>=a:
        break
    
print(s)

#6087 : [기초-종합] 3의 배수는 통과(설명)(py)
#3 배수만 출력하지 말자
a = int(input())

for i in range(1,a+1):
    if i % 3 == 0:
        continue
    print(i,end=' ')

#6088 : [기초-종합] 수 나열하기1(py) 등차수열
# a = 시작값 b = 등차값 n = 몇번째 찾고 싶은지
a, d, n = map(int, input().split())
print(a+d*(n-1))
