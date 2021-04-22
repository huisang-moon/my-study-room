#1.문자열 반복
s = int(input())
for i in range(s):
    a,b = input().split()
    a = int(a)
    b = str(b)
    for i in range(len(b)):
        print(a * b[i],end='')
    print()

#2.단어 공부

word = input().upper()
world_list = list(set(word)) 
cnt = list() 

for i in world_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(world_list[cnt.index(max(cnt))].upper())

#3. 상수
num_1 , num_2 = map(int, input().split()) 
num_1 = int(str(num_1)[::-1])
num_2 = int(str(num_2)[::-1])
if num_1 > num_2:
    print(num_1)
else:
    print(num_2)
#4 2007년

x , y = map(int, input().split())
day = 0  # 총 값 여기서 /7

month_1 = [31,28,31,30,31,30,31,31,30,31,30,31] # 0~11(index)
요일 = ["SUN","MON","TUE","WED","THU","FRI","SAT",]
for i in range(x-1):
    day += month_1[i]
day += y

print(요일[day % 7])

#5 그대로 출력하기
while True:
    try:
        print(input())
    except EOFError:
        break

    
#6 열 개씩 끊어 출력하기

n = input()
for i in range(0,len(n),10):
    print(n[i:i+10])

#7 그대로 출력하기 -2

while True:
    try:
        print(input())
    except EOFError:
        break

#8 음계
n = list(map(int, input().split()))

if n == sorted(n):
    print("ascending")
elif n == sorted(n,reverse=True):
    print("descending")
else:
    print("mixed")

#9 다이얼

word = input().upper()
alphabat = list(["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"])
second = 0 

for i in range(len(word)):
    for j in alphabat:
        if word[i] in j:
            second += alphabat.index(j) + 3
print(second)

#10 그룹 단어 체커

num = int(input())
group_word = 0 

for i in range(num):
    num_2 = input()
    error = 0 #그룹단어 아닌 것
    for j in range(len(num_2)-1):
        if num_2[j] != num_2[j+1]: #연달아 나오는 문자가 다를 때
            new_num = num_2[j+1:]
            if new_num.count(num_2[j]) > 0:
                error += 1
    if error == 0 :
        group_word += 1
print(group_word)





