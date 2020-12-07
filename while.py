# 10진수를 2진수로 변환하는 프로그램
n = int(input('Number: '))
result = ''

while n != 0:
    m = n % 2
    result = str(m) + result
    n = n // 2
    
print(result)
