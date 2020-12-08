# 임의의 자연수 n이 입력되면 2부터 n까지의 모든 소수를 출력하는 프로그램
# 소수는 1과 자기자신으로만 나누어 떨어지는 수.
i =2
num = int(input("숫자를 입력하세요."))
for i in range(2, num+1, 1):
    isprime= True
    for n in range(2, i, 1):
        if(i%n==0):
            isprime = False
            break
    if(isprime==True):
        print(i)