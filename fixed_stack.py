#스택(stack)은 데이터를 임시 저장할 때 사용하는 자료구조, LIFO방식 입니다(후입선출)
#넣는 방식 푸쉬 / 꺼내는 것 팝
#스택 배열 : STK / list형  본체
#스택 크기 : capacity / 스택의 최대 크기를 나타내는 int형 정수입니다. <-> 이 값은 배열 stk의 원소 수인 len(stk)와 일치 합니다.
#스택 포인터 : ptr / 쌓여 있는 데이터 수
#calss FixedStack 사용
#실습 4 - 1 [A]
#고정 길이 스택 클래스 FixedStack 구현하기

from typing import Any

class FixedStack: #고정 길이 스택 클래스
    
    class Empty(Exception): #exception :예외 -> 비어있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity : int = 256) -> None: #스택 초기화 #모든 원소가 none이다
        self.stk = [None] * capacity # 스택 본체
        self.capacity = capacity #스택의 크기
        self.ptr = 0 #스택 포인터 하나도 안쌓여 있다
    
    def __len__(self) -> int: #스택에 쌓여있는 데이터 개수를 반환  / __len__() 쌓여있는 데이터 개수를 알아내는 함수이다.
        return self.ptr
    
    def is_empty(self) -> bool:
        return self.ptr <= 0 # 스택이 비어 있는지 판단
    
    def is_full(self) -> bool:
        return self.ptr >= self.capacity
        #스택이 가득 차 있는지 판단

    def push(self, value: Any) -> None:
        #스택에 value를 푸시(데이터를 넣음)
        if self.is_full(): #스택이 풀방일 경우
            raise FixedStack.Full #raise 강제로 에러 발생
        self.stk[self.ptr] = value
        self.ptr +=1
    def pop(self) -> Any: #스택에서데이터를 팝
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0 # 모두 비움

    def find(self,value : Any) -> Any:
        #스텍에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)
        for i in range(self.ptr -1, -1, -1): #꼭대기부터 선현검색으로 올라감
            if self. stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> bool:
        #스택에 있는 value의 개수를 반환
        c = 0 
        for i in range(self.ptr):
            if self.sti[i] == value: #바닥부터 선형검색
                c += 1
            return c

    def __contains__(self, value: Any) -> bool:
        #스택에 value가 있는지 판단
        return self.count(value)

    def dump(self) -> None:
        #dump는 모든 데이터를 바닥부터 꼭대기 순으로 출력
        if self.is_empty():
            print('스택이 비어있습니다')
        else:
            print(self.stk[:self.ptr])
            