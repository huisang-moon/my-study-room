#1 큐2
import sys
n = int(sys.stdin.readline())
array = list()
count = 0 #count는 인덱스야 큐는 앞에서부터 뺴니까 뺼때마다 당겨주면 시간 초과.

for i in range(n):
    a = sys.stdin.readline().split()
    
    if a[0] == 'push':
        array.append(a[1])
    elif a[0] == 'pop': 
        if len(array) > count: 
            print(array[count]) 
            count += 1 
        else:
            print('-1') #배열 안에 아무것도 없으면 -1을 출력.
    elif a[0] == 'size' :
        print(len(array)-count)
    elif a[0] == 'empty':
        if len(array) == count:
            print('1')
            count = 0
            array = []
        else:
            print('0')
    elif a[0] == 'front':
        if len(array) > count :
            print(array[count])
        else:
            print('-1')
    elif a[0] == 'back':
        if len(array) > count :
            print(array[-1])
        else:
            print('-1')
    

    #2 카드2 #큐는 리스트를 사용하지 않는당 (시간 복잡도 연관)
import sys
from collections import deque

n = int(sys.stdin.readline())
array = deque([i for i in range(1,n+1)])
count = 0

while len(array) > 1:
    array.popleft()
    array.append(array.popleft()) #popleft 제일 왼쪽거

print(array.pop()) # 팝은 꺼내는 것
            
#3.요세푸스 문제 
import sys

n , k = map(int,sys.stdin.readline().split())

array = [i for i in range(1,n+1)]
result = list()
index_temp = k - 1 #제로 인덱스이기 때문에

for i in range(n):
    #리스트 넘지 않으면
    if len(array) > index_temp :
        result.append(array.pop(index_temp))
        index_temp += k-1 # 다음 인덱스
    elif len(array) <= index_temp:
        index_temp = index_temp % len(array)
        result.append(array.pop(index_temp))
        index_temp += k-1

print('<',end='')
for i in result:
    if i==result[-1]:print(i,end='')
    else: print("%s, "%(i),end='')
print('>',end='')            

#4.덱 기본
import sys
from collections import deque

n = int(sys.stdin.readline())
array = deque()




for i in range(n):
    b = sys.stdin.readline().split()

    if b[0] == 'push_front':
        array.appendleft(b[1])
    elif b[0] == 'push_back':
        array.append(b[1])
    elif b[0] == 'pop_front':
        if len(array) > 0:
            temp = array.popleft()
            print(temp)
        else:
            print('-1')
    elif b[0] == 'pop_back':
        if len(array) > 0 :
            print(array[-1])
            array.pop()
        else:
            print('-1')
    elif b[0] =='size':
        print(len(array))
    elif b[0] =='empty':
        if len(array) == 0:
            print(1)
        else:
            print(0)
    elif b[0] == 'front':
        if len(array) > 0 :
            print(array[0])
        else:
            print(-1)
    elif b[0] == 'back':
        if len(array) > 0:
            print(array[-1])
        else:
            print(-1)

    
