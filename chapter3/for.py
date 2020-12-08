# for 문

for i in [1,2,3]: # 끝에 :
    print("숫자", i) # 들여쓰기

for i in(1,2,3):
    print("숫자", i)

for i in "hello":
    print(i)

for i in range(1,4,1): #1부터 시작하여 1씩 증가하여 4가 되면 종료
    print("Number", i) #들여쓰기

# 중첩 반복문
# 구구단
for i in range(2,10,1):
    for j in range(1, 10, 1):
        print("%d x %d = %d" %(i,j,i*j))

# 무한 반복문
# while True:
#     print("last forever")
# 무한 반복문을 중지하려면 Ctrl + c