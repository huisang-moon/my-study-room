#1.각 열에 퀸을 1개 배치하는 조합 
#2.각 행에 퀸을 1개씩만 배치한다
#3.8퀸 알고리즘 구현

pos = [0] * 8 #각 열에서 퀸의 위치
flag_a = [False] * 8 #각 행에 퀸을 배치했는지 체크 
flag_b = [False] * 15 #↗↙
flag_c = [False] * 15 # 대각선 ↖↘

def put() -> None:
    for i in range(8):
        for j in range(8):
            print("●" if pos[i]==j else "○", end=' ')
        print()
    print()

def set(i: int) -> None:
    for j in range(8):
        if (not flag_a[j]
        and not flag_b[i+j] # 대각선 ↗↙
        and not flag_c[i-j+7] ): # 대각선 ↖↘
            pos[i] = j #퀸을 j행에 배치
            if i == 7: #모든 열에 퀸을 배치 완료
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[ i - j +7] = True
                set(i+1) #i가 열이야 j값이 행
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False

set(0)
