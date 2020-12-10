# 원의 면적 및 둘레 구하기 함수를 이용해서
pi = 3.14

def cir_area(r):
    area = pi*r**2
    return area

def cir_cirm(r):
    cirm = pi*2*r
    return cirm

a=cir_area(4)
b=cir_cirm(4)

print('%.1f' %a)
print('%.1f' %b)