# 리스트[1,2,3]에 대해 다음과 같이 처리

list=[1,2,3]
# 1. 두 번째 요소를 17로 수정
list[1]=17
print(list)

# 2. 리스트에 4,5,6을 추가
list1=list +[4,5,6]
print(list1)

# 3. 첫 번째 요소 제거
del(list1[0])
print(list1)

# 4. 리스트를 요소 순서대로 배열
list1.sort()
print(list1)

# 5. 인덱스 3에 25넣기
list1[3]=25
print(list1)