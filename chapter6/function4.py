# 함수를 이용하여 10진수를 2진수로 변환하는 프로그램
# n = int(input('Number: '))

# def dec2bin_int(n):
#     result = ''
#     while n != 0:
#         m = n%2
#         result = str(m) + result
#         n = n // 2
#     return result

# print(dec2bin_int(n))

# 1보다 작은 소수를 2진수로 변환

def dec2bin_float(n):
    result = ''
    while n>0:
        n = n*2 
        if n >= 1:
            result=result+'1'
            n=n-1
        else:
            result=result+'0'
        if len(result) >1000:
            break
    return '0.'+result

print(dec2bin_float(0.125))

# 실수 n을 2진수로 변환

# def dec2bin(n): 
#     result1 = ''
#     result2 = ''
#     n1=int(n)
#     n2=n-n1
#     while n1 != 0:
#         m = n1%2
#         result1 = str(m) + result1
#         n1 = n1 // 2
    
#     while n2>0:
#         n2 = n2*2 
#         if n2 >= 1:
#             result2=result2+'1'
#             n2=n2-1
#         else:
#             result2=result2+'0'
#         if len(result2) >1000:
#             break
#     return result1 + '.' +result2

# print(dec2bin(12.125))
