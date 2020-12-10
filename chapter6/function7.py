# 두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램

# num1=int(input("첫번째 숫자 입력."))
# num2=int(input("두번째 숫자 입력."))
# def pyramid(n1, n2):
#     for i in range (0,n1):
#         print("*"*int(n2))

# pyramid(num1, num2)

# 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성
# 예 : 123 -> 1+2+3=6
# num=input("숫자를 입력하세요")
# def num1(num):
#     sum=0
#     for i in num:
#         sum+=int(i)
#     return sum

# a=num1(num)
# print(a)

# 두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성.
# 두 개의 문자열이 같으면 -1을 반환
# string='abcek'
# string2='abcekghk'
# def func(a, b):
#     c=b
#     if a==b:
#         return -1
#     if len(a) <= len(b):
#         c=a
#     for i in range(0, len(c)):
#         if a[i]!=b[i]:
#             return i
#     return len(c)

# k= func(string,string2)
# print(k)

# 숫자를 전달받아 그 수의 약수를 리스트로 반환하는 함수
# num=int(input("숫자를 입력하세요"))
# def divisor(n):
#     result =[]
#     for i in range(1, n+1):
#         if n % i == 0:
#             result.append(i)
#     return result

# a= divisor(num)
# print(a)

# 문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아
# 리스트로 반환하는 함수를 작성
# string=input("문자열을 입력하세요.")
# char=input("하나의 문자를 입력하세요.")
# result=list(string)
# result2=[]
# def func(string, char):
#     for i in range(0, len(string)):
#         if result[i]==char:
#          result2.append(i)
#     return result2

# a= func(string, char)
# #print("입력하신", char, "문자가 들어있는 위치는", a,"입니다") 
# print(f"입력하신{char} 문자가 들어있는 위치는 {a}입니다")

# 재귀 함수를 이용하여 1부터 100까지 합을 계산 
# 재귀 함수는 base 까지 가는 것을 먼저 생각해야 함. 그리고는 return 하면서 값 더해짐.

a=int(input("1부터 n까지 합을 계산합니다. 자연수 n을 입력하세요."))
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)

print(sum(a))