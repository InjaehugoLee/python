# 리스트 요소 순서 나열
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #오름차순으로 배열
print(cars)

cars.sort(reverse=True) #역순 배열
print(cars)

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars)) # 오름차순으로 배열한 리스트를 따로 생성
print("\nHere is the original list again:")
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
