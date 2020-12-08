# 두 수의 최대 공약수는 두 수를 나누어 떨어지는 가장 큰 수이다.
# 예를 들어, (16, 24)의 최대 공약수는 8이다. 두 수를 입력받아
# 다음 알고리즘에 의해 최대 공약수를 구하는 프로그램을 작성하라.

# 조건 1. 큰 수를 작은 수로 나눈 나머지를 구하라.
# 조건 2. 큰 수를 작은 수로 대체하고 작은 수는 나머지로 대체하라
# 조건 3. 작은 수가 0이 될 때까지 이 과정을 반복하라. 마지막 큰 수가 최대 공약수이다.


num1 = int(input("첫 번째 숫자를 입력하세요."))
num2 = int(input("두 번째 숫자를 입력하세요."))
num_max = 0
num_min = 0
if num1 > num2:
    num_max = num1
    num_min = num2
else: 
    num_max = num2
    num_min = num1

while num_min!=0:
    num3 = num_max % num_min
    num_max = num_min
    num_min = num3
    if num_min == 0:
        print("최대공약수는 : ", num_max)
        break
    


    