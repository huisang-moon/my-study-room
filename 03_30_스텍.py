#1 스택
import sys

n = int(sys.stdin.readline())
stack = list()

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        stack.append(int(a[1]))
    elif a[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else: 
            print(stack.pop())
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    elif a[0] == 'top':
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack[-1])

            
#2제로 
import sys

k = int(sys.stdin.readline())
stack = list()

for i in range(k):
    a = int(sys.stdin.readline()) #여기서 append 쓰면 안댕 다 확인하고 들어가야 해!
    if a == 0 :
        stack.pop()
    else :
        stack.append(a)


print(sum(stack))

#3 괄호 

import sys
t = int(sys.stdin.readline())
for i in range(t):
    stack = list()
    vps = sys.stdin.readline()
    check = 0 # 스텍 내부 확인용
    for j in vps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0: #처음이면
                print("NO")
                check = 1 # 스텍 내부가 비어있다.
                break
            else:
                stack.pop(-1) #스택이 안 비어있으니 ( 꺼내서 () 만들어랑
    if len(stack) != 0 and check == 0:
        print('NO')
    elif len(stack) == 0 and check == 0: #check = 1 비었다 check = 0 들어있다
        print('YES')

#4 균형잡힌 세상
import sys
while True:
    t = sys.stdin.readline()
    stack = list()
    check = True
    if t == '.':
        break

    for i in t:
        if i == '(' or i == '[' :
            stack.append(i)
        
        elif i == ")":
            if len(stack) == 0:
                check = False
                break
            if stack[-1] == "(":
                stack.pop()
            else:
                check = False
                break
        elif i == "]":
            if len(stack) == 0:
                chekc = False
                break
            if stack[-1] == "[":
                stack.pop()
            else:
                check = False
                break
    if check and not stack: # not stack == 스택이 비어져 있다.
        print("yes")
    else:
        print("no")

        