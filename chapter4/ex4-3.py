# 숫자를 문자열로 변환하는 방법은 str(num)을 이용
# str(12) -> '12'가 된다.
# 반대로 문자열을 숫자로 변환하려면  int(string)을 이용
# int('12')-> 12가 된다. 
# 1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하라

n=int(input("정수를 입력하십시오 : "))
sum=0
for i in range(1,n+1):
    sum1=0
    for s in str(i): # 숫자 i를 문자열로 해석해서 각 단위를 따로 뽑아서 s에 넣음
       sum+=int(s)
       sum1+=int(s)
    print(i,sum1)
print(sum)
