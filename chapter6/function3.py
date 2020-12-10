# 함수를 이용해서 약수 구하기
def den(n):
    result=[]
    for i in range(1, n+1):
        if n%i==0:
            result.append(i)
    return result  

a= den(12)
print(a)