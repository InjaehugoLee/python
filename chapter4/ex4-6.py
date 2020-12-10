# for 루프를 이용하여 다음과 같은 리스트 생성

# 1. 0~49까지의 수로 구성되는 리스트
# list2=[]
# for i in range(0, 50):
#     list2.insert(i, i)
#     #list2.append(i)
# print(list2)

# # 2. 1~50까지 수의 제곱으로 구성되는 리스트
# list3=[]
# for i in range(1, 51):
#     list3.insert(i, i*i)
#     #list3.append(i**2)
# print(list3)

# 크기가 같은 두 개의 리스트 L, M을 생성하고 
# 각 요소 합으로 구성되는 새로운 리스트를 생성
# 예를 들어, L=[1,2,3]이고 M=[4,5,6]이면 [5,7,9]

# L=[1,2,3]
# M=[4,5,6]
# list4=[]
# for i in range(0, 3):
#     list4.append(L[i]+M[i])
# print(list4)

# 사용자로부터 5개의 숫자를 문자열로 입력 받아 각 숫자를 +로 연결한 문자열 생성
# 예, 2,5,11,33,55 입력시, '2+5+11+33+55' 생성

a=input("숫자를 입력하세요.")
# 1.
#print(a.replace(' ', '+'))

# 2.
S=''
L=a.split()
for i in range(0, len(L)):
    if i!=0:
        S+='+'
    S+=(L[i])
print(S)       

# 3.
L=a.split()
for i in range(0, len(L)):
    if i!=0:
        print('+', end='')
    print(L[i], end='')

