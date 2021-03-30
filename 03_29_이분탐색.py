#1 수 찾기
# N , M
import sys


n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split())) # 배열로 1, 2 ,3, 4 ,5 받음
A = sorted(A)

m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
B = sorted(B)

#이것은 선형검색이당.
for i in range(m):
    if B[i] in A:
        print("1")
    else:
        print("0")
# pc = (pl + pr) // 2 pl = 0 pr = len() - 1

#1 수 찾기 이진검색
# N , M
import sys


n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split())) # 배열로 1, 2 ,3, 4 ,5 받음
A = sorted(A)

m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

def binary(arr,val,pl,pr): #여기가 이진검색 함수
    if pl > pr:
        return False
    pc = (pl + pr) // 2
    if arr[pc] > val:
        return binary(arr,val,pl,pc-1)
    elif arr[pc] < val:
        return binary(arr,val,pc+1,pr)
    else:
        return True

for i in B:
    if binary(A,i,0,n-1):
        print(1)
    else:
        print(0)



#2.숫자 카드2 / 해시법 접근!
import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
nlist = sorted(nlist)

m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))

dic = dict() #python은 해시가 딕셔너리로 구성되어 있다.

for i in nlist:
    try:
        dic[i] += 1
    except:
        dic[i] = 1
for i in mlist:
    try:
        print(dic[i], end=' ')
    except:
        print(0, end=' ')
        
#3.랜선 자르기
import sys

k , n = map(int, sys.stdin.readline().split())
arr = list()
for i in range(k):
    arr.append(int(sys.stdin.readline()))
short_band , long_band = 1 , max(arr) #최소길이는 1cm ~ 최대길이는 주어진 것 중 최대
result = 0 

while short_band <= long_band:
    mid = (short_band + long_band) // 2 # 몇 cm로 잘라낼건가 
    cut_sum = sum([(i // mid) for i in arr]) #각각 잘라낸 것들 갯수
    
    #갯수로 판단하는 거지 k개를 n개로 만들었느냐.
    if cut_sum >= n: # 잘라낸게 필요보다 많을시
        result = mid 
        short_band = mid + 1
    elif cut_sum < n: #잘라낸게 적을시 
        long_band = mid - 1
print(result)


#4 나무 자르기 
import sys

n,m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    result = 0

    for i in tree:
        if i >= mid:
            result += i - mid
    
    if result >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)


#5 공유기 설치
import sys
n,c = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for i in range(n)])

left = 1
right = max(house) - min(house)
result = 0

while right >= left :
    mid = (left + right) // 2
    count = 1 # 와이파이 첨에 1개 설치되어 있다.
    the_house = house[0] # 첫번째 인덱스에 공유기가 설치되어 있다/ 우리는 최소 거리 찾기가 중요
    
    for i in range(1,n): # 1부터 시작은 0 인덱스 집은 설치 되어 있으니 집 거리 늘리면서 찾기
        if house[i] >= the_house + mid : #설치 간격 충족 
            count += 1
            the_house = house[i] #공유기가 최근 설치된 집
    if count < c:
        right = mid - 1
    elif count >= c:
        left = mid + 1
print(count)

#5 공유기 설치
import sys
n,c = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for i in range(n)])

left = 1
right = max(house) - min(house)
result = 0

while right >= left :
    mid = (left + right) // 2
    count = 1 # 와이파이 첨에 1개 설치되어 있다.
    the_house = house[0] # 첫번째 인덱스에 공유기가 설치되어 있다/ 우리는 최소 거리 찾기가 중요
    
    for i in range(1,n): # 1부터 시작은 0 인덱스 집은 설치 되어 있으니 집 거리 늘리면서 찾기
        if house[i] >= the_house + mid : #설치 간격 충족 
            count += 1
            the_house = house[i] #공유기가 최근 설치된 집
    if count < c:
        right = mid - 1
    elif count >= c:
        left = mid + 1
print(count)

