# 정수 N개의 합
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
def solve(a):
    return sum(a)

# 셀프 넘버
# 리스트 풀이
numbers = list(range(1,10000+1))
remove_list = list()

for num in numbers:
    for i in str(num):
        num += int(i)
    if num <= 100000:
        remove_list.append(num)

for remove_num in set(remove_list): #중복 제거해서 새로운 remove_num에 넣고
    numbers.remove(remove_num) #새로 정리된 remove_num의 숫자 <- 생성자를 기존 numbers 1~10000까지 있는 곳에 합쳐서 제거 해주면 셀프넘버만 남는다
for self_num in numbers: # numbers에 제거된거 남았잖아
    print(self_num)

# 셀프 넘버
# 집합풀이

numbers = set(range(1,10000+1))
remove_set = set()
for num in numbers:
    for n in str(num):
        num += int(n)
    remove_set.add(num) #set()에서는 추가시 add()를 사용하여 추가한다

self_number = numbers - remove_set #차집합 전체에서 - 생성자
for self_number in sorted(self_number):
    print(self_number)

#한수
import sys
num = int(sys.stdin.readline())
hansu = 0

for i in range(1,num + 1):
    if i <= 99:
        hansu += 1
    else:
        nums = list(map(int,str(i))) #먼저 문자로 쪼개고/ 그것을 인트로 리스트에 저장
        if nums[0] - nums[1] == nums[1] - nums[2] : #등차 확인
            hansu += 1
print(hansu)

#팩토리얼
import sys

def factorial(a):
    if a > 0:
        return a * factorial(a-1)
    else:
        return 1

n = int(sys.stdin.readline())
print(factorial(n))

#별찍기 - 10 (프랙탈구조) -> 분할,정복 알고리즘 이해 필요
#이거는 다시 한 번 이해하고 풀어볼 필요 있음.

def stars(n):
    matrix=[]
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

star = ["***","* *","***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1
    
for i in range(k):
    star = stars(star)
for i in star:
    print(i)
