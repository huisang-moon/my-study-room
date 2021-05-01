#1 프린터 큐
num = int(input())

for i in range(num):
    a , b = map(int,input().split())
    
    k = list(map(int, input().split()))
    chec = [0 for j in range(a)]
    chec[b] = 1 #궁금한거 위치 고정
    
    count = 0 
    while True:
        if k[0] == max(k):
            count += 1

            if chec[0] != 1:
                del k[0]
                del chec[0]
            else:
                print(count)
                break
        else:
            k.append(k[0]) # append는 뒤로 들어간다
            chec.append(chec[0])
            del k[0] 
            del chec[0]
  
test = int(input())
for i in range(test):
    n , m = map(int, input().split())
    imp = list(map(int, input().split()))
    check_list = [0 for j in range(n)]
    check_list[m] = 1
    
    count = 0
    while True:
        if imp[0] == max(imp):
            count += 1
            if check_list[0] != 1 :
                del imp[0]
                del check_list[0]
            else:
                print(count)
                break
        else:
            imp.append(imp[0])
            check_list.append(check_list[0])
            del imp[0]
            del check_list[0]    
    
#2 검증 수
검증수 = list(map(int,input().split()))
arr = []
for i in range(len(검증수)):
    a = pow(검증수[i],2)
    arr.append(a)
b = sum(arr) % 10
print(b)

#3 별찍기 - 6
n = int(input())

for i in range(n,0,-1):
    print( " " * (n-i) +"*" * i + "*" *(i-1))

#4. 이항 계수 1

from math import factorial 

n , k = map(int,input().split())
print(factorial(n)//(factorial(k)*factorial(n-k)))

#5 방 번호[1475]

room_number = str(input())
card = [0 for i in range(10)]

for i in room_number:
    if i == '6' or i =='9':
        if card[6] == card[9]:
            card[6] += 1
        else:
            card[9] += 1
    else:
        card[int(i)] += 1 # i는 str이기 때문에 int로 바꿔줘야함
print(max(card))

#6 윷놀이[2490]
for i in range(3):
    draw = list(map(int, input().split()))
    count = 0
    for j in range(4):
        if draw[j] == 0 :
            count += 1
    if count == 1 :
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    elif count == 4:
        print("D")
    else:
        print("E")