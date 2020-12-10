# 정수를 입력 받아 그 수의 약수를 모두 출력하는 프로그램을 작성
# m % n = 0이면 n은 m의 약수이다. 예를 들어 12의 약수는 1,2,3,4,6,12

num = int(input("정수를 입력하세요."))
for i in range(1, num+1, 1):
    answer = num % i
    if(answer == 0):
        print(i,end=' ') # end 옆으로 출력