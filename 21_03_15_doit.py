#실습예제 3-1 선형 검색 알고리즘
#while 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1

if __name__ =='__main__' : #여기가 시작이당~
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num #여기 리스트에 담을거임 왜냐면 sequence를 사용했으니까

    for i in range(num):
        x[i] = int(input("x[{}]:".format(i)))
    
    ky = int(input("검색할 값을 입력하세요.:"))

    idx = seq_search(x, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print('검색값은 x[{}]에 있습니다.'.format(idx))

#실습예제 3-2 선형 검색 알고리즘
#while 문을 ->for문으로 더 간단하게 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    for i in range(len(a)):
        if a[i] == key:
            return i
        return -1

if __name__ =='__main__' : #여기가 시작이당~
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num #여기 리스트에 담을거임 왜냐면 sequence를 사용했으니까

    for i in range(num):
        x[i] = int(input("x[{}]:".format(i)))
    
    ky = int(input("검색할 값을 입력하세요.:"))

    idx = seq_search(x, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print('검색값은 x[{}]에 있습니다.'.format(idx))

#이 두 방법은 배열의 순서가 정해져있지 않을 경우에 사용되는 것이다.

#보초법 실습예제 3-3 
#여기서는 import copy 와 deepcopy 이게 주요함

from typing import Sequence, Any
import copy

def seq_search(seq : Sequence, key: any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0 
    while True:
        if a[i]==key:
            break
        i+=1
    return -1 if i ==len(seq) else i

if __name__ =='__main__':
    num = int(input('원소 수를 입력하세요.:'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input("x[{}]".format(i)))
    
    ky = int(input('검색할 값을 입력하시오.:'))

    idx = seq_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print('검색값은 x[{}]에 있습니다.'.format(idx))
        
#예제 실습 3-4 이진 검색 알고리즘
from typing import Any, Sequence

def bin_search(a: Sequence, key: any) -> int:
    pl = 0
    pr = len(a) -1 #제로 인덱스라 그럼 (인덱스 기준)
    while True:
        pc = (pl + pr) //2 
        if a[pc] == key:
            return pc
        elif a[pc] <key:
            pl = pc +1
        else:
            pr = pc - 1
        if pl >pr :
            break
        return -1

if __name__ == "__main__":
    num = int(input("원소 수를 입력하시오:"))
    x = [None] * num
    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input("x[0]: "))

    for i in range(1, num):
        while True:
            x[i] = int(input("x[{}]:".format(i)))
            if x[i] >= x[i - 1]:
                break

    ky = int(input('검색 값을 입력하시오.:'))

    idx = bin_search(x,ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print('검색값은 x[{}]에 있습니다'.format(idx))
