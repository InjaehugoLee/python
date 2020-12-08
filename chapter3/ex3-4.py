# 다음과 같은 게임 프로그램을 작성하라.
# 플레이어가 처음에 $50을 가지고 있다. 동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다.
# 맞추면 $9을 따고 틀리면 $10을 잃는다. 
# 플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다
# 동전을 던져서 나오는 수는 다음 문장을 이용하라

money = 50

from random import randint
num_count = 0
while money >= 0 or money <= 100:
    coin = randint(1,2)
    answer = int(input("앞면(1), 뒷면(2) 을 고르세요.\n"))
    if coin == answer:
        money = money + 10
        num_count= num_count+1
        print("정답입니다. $10를 벌었습니다. 값은 : \n", money)
        if money <= 0 or money >= 100:
            break
    else:
        money = money - 9
        num_count= num_count+1
        print("틀렸습니다. $9을 잃었습니다. 값은 :\n", money)
        if money <= 0 or money >= 100:
            break
