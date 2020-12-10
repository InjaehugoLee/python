# index를 이용하여 문자열의 문자를 역순으로 출력

outStr = "" # 변수 초기화(빈 문자열)
count, i = 0, 0

##메인 코드 부분##
inStr=input("Type string:")
count=len(inStr) #문자열 길이

for i in range(0, count):
    outStr += inStr[count-(i+1)] # 마지막 문자부터 추출하여 저장
print("Reversed string: %s" %outStr)