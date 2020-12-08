# 초를 입력하면 분과 초로 표시하는 프로그램. 예) 200초 입력시 3분 20초
sec = int(input("초를 입력하세요:"))
min_sec1 = sec / 60 
min_sec2 = sec % 60 
print("입력한 초를 분으로 환산시 : %d" %min_sec1, "분", "%d" %min_sec2, "초")