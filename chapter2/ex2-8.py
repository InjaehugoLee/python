# 판매자가 딸기와 포도를 판매. 포도 한 알의 무게 75g, 딸기 한 알의 무게 113.5g. 
# 사용자로부터 포도 알의 개수와 딸기의 개수를 입력 받아 총 무게를 계산하여 출력하는 프로그램을 작성
g_weight = 75
s_weight = 113.5
g_quantity = int(input("먹고 싶은 포도의 개수는?"))
s_quantity = int(input("먹고 싶은 딸기의 개수는?"))
sum = (g_weight * g_quantity) + (s_weight * s_quantity)
print("총 무게는 : %5.2f" %sum, "g")