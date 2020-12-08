# 사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력 받는다.
# 또, "am" 혹은 "pm"을 입력 받고 경과 시간을 나타내는 값을 입력 받는다.
# 이로부터 최종 시간이 몇 시인지 출력하는 프로그램 작성

hour = int(input("Enter hour. 1~12 :"))
time = int(input("am이면 숫자 1입력, pm이면 숫자 2입력 :"))
a_time = int(input("How many hours ahead? : "))
sum = hour + a_time
result1 = sum % 12
result2 = sum // 12
if (sum > 12):
    if(result2 % 2 == 0):
        if(time == 1):
            print("%d am" %result1)
        else:
            print("%d pm" %result1)
    elif(result2 % 2 == 1):
        if(time == 1):
            print("%d pm" %result1)
        else:
            print("%d am" %result1)
elif(sum < 12):
    if(time == 1):
        print("%d am" %sum)
    else:
        print("%d pm" %sum)
else:
    if(time == 1):
        print("%d am" %sum)
    else:
        print("%d pm" %sum)