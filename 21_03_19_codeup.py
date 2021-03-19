#6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

print(min(a))

#6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)

d = []
for i in range(19):
    d.append([])
    for j in range(19):
        d[i].append(0)
#d = [0 for i in range(19)] for j in range(19) ]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    d[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j],end=' ')
    print()

#6096 : [기초-리스트] 바둑알 십자 뒤집기(py)
#a = [[]*19 for _ in range(19)]
#for i in range(19):
 #  a[i]=list(map(int,input().split()))

a = [[0 for i in range(19)] for j in range(19)]

n = int(input())

for i in range(n):
    x,y = map(int, input().split())
    for j in range(19):
        if a[j][y-1] == 0:
            a[j][y-1] = 1
        else:
            a[j][y-1] = 0
    
        if a[x-1][j] == 0:
            a[x-1][j] = 1
        else:
            a[x-1][j] = 0

for i in range(19):
    for j in range(19):
        print(a[i][j],end=' ')
    print()

#6097 : [기초-리스트] 설탕과자 뽑기(py)

h, w = map(int, input().split())

n = int(input())

board = [[0]*w for i in range(h)]

for i in range(n):
    l,d,x,y = map(int, input().split())
    if d == 0:
        for j in range(l):
            board[x-1][y-1+j] = 1
    else:
        for j in range(l):
            board[x-1+j][y-1] = 1

for i in range(h):
    for j in range(w):
        print(board[i][j],end=' ')
    print()

    #
    h,w = input().split()
h = int(h)
w = int(w)

m = []
for i in range(h+1) :
  m.append([])
  for j in range(w+1) :
    m[i].append(0)

n = int(input())
for i in range(n) :
  l,d,x,y = input().split()
  if int(d)==0 :
    for j in range(int(l)) :
      m[int(x)][int(y)+j] = 1
  else :
    for j in range(int(l)) :
      m[int(x)+j][int(y)] = 1

for i in range(1, h+1) :
  for j in range(1, w+1) :
    print(m[i][j], end=' ')
  print()


#6098 : [기초-리스트] 성실한 개미(py)

#입력에서 직접 맵 개설
board = [[]*10 for i in range(10)]
for i in range(10):
    board[i] = list(map(int, input().split()))

x = 1
y = 1
board[x][y] = 9

while True:
    if(board[x][y]==2):
        board[x][y]=9
        break
    if(board[x][y+1]!=1):
        board[x][y]=9
        y+=1
    else:
        if(board[x+1][y]!=1):
            board[x][y]=9
            x+=1
        else:
          board[x][y]=9
          break

for i in range(10):
    for j in range(10):
        print(board[i][j],end=' ')
    print()