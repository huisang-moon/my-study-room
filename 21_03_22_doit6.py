#버블 정렬 알고리즘 구현하기 6-1

from typing import MutableSequence

def bubble_sort(a : MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i , -1):
            if a[j-1] > a[j]:
                a[j - 1], a[j] = a[j], a[j-1]

if __name__ == '__main__' :
    print('버블 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: ')) #x[0]: 이렇게 나옴

    bubble_sort(x) #함수 호출

    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


#버블 정렬 알고리즘 구현하기 6-2 정렬 과정 출력

from typing import MutableSequence

def bubble_sort_verbose(a : MutableSequence) -> None:
    ccnt = 0
    scnt = 0
    n = len(a)
    for i in range(n-1):
        print(f'패스 {i+1}')
        for j in range(n-1, i , -1):
            for m in range(0, n-1):
                print(f'{a[m]:2}' + ('  ' if m != j -1 else ' + ' if a[j-1] >a [j] else '-' ),end=' ')
                print(f'{a[n -1]:2}')
                ccnt += 1
                if a[j-1] > a[j]:
                    scnt += 1
                    a[j - 1], a[j] = a[j], a[j-1]
        for m in range(0 , n-1):
            print(f'{a[m]:2}', end= ' ')
        print(f'{a[n-1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

if __name__ == '__main__' :
    print('버블 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: ')) #x[0]: 이렇게 나옴

    bubble_sort_verbose(x) #함수 호출

    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


#버블 정렬 알고리즘 구현하기 6-3 알고리즘 개선

from typing import MutableSequence

def bubble_sort(a : MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        exchng = 0 # 패스에서 교환 횟수
        for j in range(n-1, i , -1):
            if a[j-1] > a[j]:
                a[j-1] , a[j] = a[j] , a[j-1]
                exchng += 1
        if exchng == 0 :
            break


if __name__ == '__main__' :
    print('버블 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: ')) #x[0]: 이렇게 나옴

    bubble_sort(x) #함수 호출

    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

#버블 정렬 알고리즘 구현하기 6-4 알고리즘 개선(2) 이미 정렬된거 빼고

from typing import MutableSequence

def bubble_sort(a : MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n-1 :
        last = n -1
        for j in range(n-1, k ,-1):
            if a[j-1] > a[j]:
                a[j-1] , a[j] = a[j] , a[j-1]
                last = j
        k = last

if __name__ == '__main__' :
    print('버블 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: ')) #x[0]: 이렇게 나옴

    bubble_sort(x) #함수 호출

    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

#버블 정렬 알고리즘 구현하기 6-5 셰이커 정렬 알고리즘

from typing import MutableSequence

def shaker_sort(a : MutableSequence) -> None:
    left = 0
    right = len(a) - 1 # n-1
    last = right 
    while left < right :
        for j in range(right, left , -1):
            if a[j-1] > a[j]:
                a[j-1] , a[j] = a[j] , a[j-1]
                last = j
        left = last
        for j in range(left, right):
            if a[j] > a[j+1] :
                a[j] , a[j+1] = a[j+1] , a[j]
                last = j
            right = last

if __name__ == '__main__' :
    print('버블 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: ')) #x[0]: 이렇게 나옴

    shaker_sort(x) #함수 호출

    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

#단순 선택 정렬 알고리즘 구현 6-6 (최소값우선)

from typing import MutableSequence

def selection_sort(a:MutableSequence) -> None:

    n = len(a)
    for i in range(n-1):
        min = i #정렬 값 가장 작은 원소의 인덱스 [4, 8 ,2, 1,3] 에서 1dms 3에 있으니 거기까지 올라감
        for j in range(i + 1, n): # 가장 작은 값을 앞으로 옮겨야 하니까 시작은 0 인덱스로
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min] , a[i]

if __name__ == '__main__' :
    print('버블 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: ')) #x[0]: 이렇게 나옴

    selection_sort(x) #함수 호출

    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')    

        #단순 선택 정렬 알고리즘 구현 6-6 (최소값우선)

from typing import MutableSequence

def selection_sort(a:MutableSequence) -> None:

    n = len(a)
    for i in range(n-1):
        min = i #정렬 값 가장 작은 원소의 인덱스 [4, 8 ,2, 1,3] 에서 1dms 3에 있으니 거기까지 올라감
        for j in range(i + 1, n): # 가장 작은 값을 앞으로 옮겨야 하니까 시작은 0 인덱스로
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min] , a[i]

if __name__ == '__main__' :
    print('버블 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: ')) #x[0]: 이렇게 나옴

    selection_sort(x) #함수 호출

    print('오름차순으로 정렬했습니다')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')    