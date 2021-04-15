#블랙잭
n, m = map(int,input().split())
array = list(map(int,input().split()))
result = 0 
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if array[i] + array[j] + array[k] > m:
                continue
            else:
                result = max(result, array[i]+array[j]+array[k])

print(result)

from itertools import combinations

n,m = map(int, input().split())
array = map(int,input().split())
result = 0 

for n in combinations(array,3):
    temp_sum = sum(n)
    if result < temp_sum <= m :
        result = temp_sum
print(result)

#분해합

n = int(input())
result = 0
for i in range(1,n+1):
    a = list(map(int,str(i)))
    result = i + sum(a) 
    if result == n:
        print(i)
        break
    if i == n:
        print(0)

