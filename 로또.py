import random, string #숫자를 확인하기 위해

cn = "y" # cn 변수는 반복문에서 빠져나오기 위한 변수로
#cn이 y인 동안 숫자를 입력받고, 입력받은 수만큼 반복한 다음 빠져나옴

print("로또 번호 자동 생성기")
print("---------------------")
print("게임 수를 입력하세요(숫자만)")

while cn == "y":
    num = input("게임수 :")
    
    if (num.isdigit()==True): #isdigit() 숫자인지 확인하는 것!
        print("---------------------------")

        for i in range(0, int(num)):
            lotto = random.sample(range(1,45+1),6)
            lotto.sort() #sort()는 오름차순!!
            print(lotto)
    else:
        print("-----------------------")
        print("숫자를 입력하세요")
        continue

    print("----------------------------")
    print("로또 번호 자동 생성 완료 ")
    print("----------------------------")

#다시 하려면 cn에 변수를 다시 받음 간단
    cn = input("다시 하시겠습니까(Y/N)? :")

    while (cn != 'y' and cn != 'n' and cn != 'Y' and cn != 'N'):
        print("y나 n만 입력하세요.")
        print("--------------------------------------")
        cn = input("다시 하시겠습니까?(Y/N)?  ")

print("-------------------------------------------")
print("로또 번호 생성 완료")
