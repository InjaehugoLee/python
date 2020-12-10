# enumerate() 내장 함수를 이용하여 사용자가 입력한 문자열에서
# 'a' 문자의 위치를 모두 찾아 출력하는 프로그램을 작성.
# 'a'가 없으면 a가 없습니다 라는 메시지 출력

# a=list(input('문자열을 입력하세요.'))
# print(a)
# b=[]
# for index, order in enumerate(a, start=1):
#     if order == 'a':
#         b.append(index)
# print(f'문자 a가 들어있는 위치는 {b} 입니다')

# 두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의
# 딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고, 
# '2'를 입력하면 sub(), '3'을 입력하면 mul(), '4'을 입력하면 div() 함수 호출
# 두 수의 연산을 수행하는 프로그램 작성.

# num1=int(input("첫 번째 숫자를 입력하세요."))
# num2=int(input("두 번째 숫자를 입력하세요."))

# def sum(a, b):
#     return a+b

# def sub(a,b):
#     c=b
#     d=a
#     if a>=b:
#         c=a
#         d=b
#     return c-d

# sum= lambda a,b: a+b
# sub = lambda a,b: abs(a-b)
# mul = lambda a,b: a*b
# div = lambda a,b: if a or b !=0: 


# def mul(a,b):
#     return a*b 

# def div(a,b):
#     c=b
#     d=a
#     if a>=b:
#         c=a
#         d=b
#     return int(c/d)
# ans= int(input('호출할 함수를 입력하세요. 1: sum, 2: sub, 3: mul, 4: div'))
# dic={1:sum(num1,num2), 2:sub(num1,num2), 3:mul(num1,num2), 4:div(num1,num2)}

# print(f'값은 : {dic.get(ans)}')

# 다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수
# 예) 문자열 'led=on&motor=off&switch=off'이고 
# 구분 문자가 '&', '='일 때 {'led': 'on', 'motor':'off', 'switch':'off'}로 반환
# Hint = dict([['a','b'],['c','d']]) --> {'a':'b','c':'d'}

# 방법 1
def func(a):
    b=a.split('&')
    #print(b)
    c=[]
    for i in range(0, len(b)):
        c.append(b[i].split('='))
    #print(c)
    d= dict(c)
    return d

print(func("led=on&motor=off&switch=off"))

# 방법 2
# def makedict(a):
#     kl=[]
#     vl=[]
#     aand=a.split('&')
#     for i in aand:  
#         kl.append(i.split('=')[0])
#         vl.append(i.split('=')[1])
#     return {key:value for key,value in zip(kl,vl)}

# print(makedict("led=on&motor=off&switch=off&wheel=ok"))