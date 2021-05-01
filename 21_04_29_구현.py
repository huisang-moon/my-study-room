#1 지능형 기차
arr = list()
people = 0
for i in range(4):
    get_out , get_in = map(int,input().split())
    people += get_in
    people -= get_out
    arr.append(people)
print(max(arr))

#2네 번째 점
squar_x = []
squar_y = []
for i in range(3):
    x , y = map(int,input().split())
    squar_x.append(x)
    squar_y.append(y)
for j in range(3):
    if squar_x.count(squar_x[j]) == 1:
        x2 = squar_x[j]
    if squar_y.count(squar_y[j]) == 1:
        y2 = squar_y[j]
print(x2,y2)

#3 날짜 계산
e,s,m,cnt = 1, 1, 1, 1
e_1 , s_1, m_1 = map(int,input().split())
while True:
    if e_1 == e and s_1 == s and m_1 == m:
        break 
    e += 1 ; s+= 1 ; m += 1 ; cnt += 1
    if e >= 16 : 
        e -= 15
    if s >= 29:
        s -= 28
    if m >=20:
        m -=19
print(cnt)
