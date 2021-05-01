#1 R2
r1 , s = map(int,input().split())

r2 = (2*s) - r1

print(r2)

#2 알파벳 개수 (10808)

s = list(str(input().lower()))
alpha = list(str('abcdefghijklmnopqrstuvwxyz'))

for i in range(len(alpha)):
    y = s.count(alpha[i])
    print(y,end=' ')

#3 단어의 길이 재기
word = input()
print(len(word))