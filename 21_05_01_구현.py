#1 로봇 청소기[14503]
n , m = map(int,input().split())
x , y , d = map(int, input().split())
board = [list(map(int,input().split())) for i in range(n)]
# for i in range(n): #n이 y값임
#     matrix = map(int,input().split())
#     board.append([matrix])

#2. 회전에 대한 정의
dx , dy = (-1 , 0 ,1 ,0 ) , (0 , 1 , 0, -1)
board[x][y] = 2 # 2는 청소 (처음 지정되면 청소한 거고 answer은 자동 1)

def solve(x,y,d,answer):
    while True:
        check = False
        for k in range(4): # 4방향 탐색
            sd = (d+3) % 4 #회전(왼쪽으로)
            next_x , next_y = x+dx[sd] , y+dy[sd] #가야할 곳
            d = sd #로봇이 보는 방향
            if not board[next_x][next_y]: #빈칸이면
                board[next_x][next_y] == 2 #청소
                answer += 1 #청소 회수 증가
                x , y = next_x , next_y
                check = True
                break
        if not check: #4 방향으로 이동이 불가
            if board[x-dx[d]][y-dy[d]] == 1: #후진시 벽
                return answer #작동 종료
            else:
                x,y = x-dx[d],y-dy[d] #후진
print(solve(x,y,d,1)) #answer이 1인 이유는 처음 자기 칸도 청소함

#1 로봇 청소기[14503]
n , m = map(int,input().split())
x , y , d = map(int,input().split())

dx = [-1 ,0 ,1 ,0]
dy = [0 , 1 , 0 , -1]

matrix = [list(map(int,input().split())) for i in range(n)]

matrix[x][y] = 2
clean = 1

while True:
    check = False
    for i in range(4):
        d = (d+3) % 4
        next_x = x + dx[d]
        next_y = y + dy[d]
        if 0 <= next_x <n and 0 <= next_y<m:
            if matrix[next_x][next_y] == 0:
                clean += 1
                matrix[next_x][next_y] = 2
                x , y = next_x , next_y
                check = True
                break
    if not check:
        next_x = x - dx[d]
        next_y = y - dy[d]
        if 0 <= next_x <n and 0 <= next_y <m:
            if matrix[next_x][next_y] ==2:
                x,y = next_x,next_y
            elif matrix[next_x][next_y] == 1:
                print(clean)
                break
        else:
            print(clean)
            break