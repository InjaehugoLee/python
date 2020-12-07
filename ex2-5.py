# 분을 입력하면 일, 시간, 분으로 출력하는 프로그램. 예) 1550분은 1일 1시간 50분
min = int(input("분을 입력하세요 : "))
day = min / 1440
hour = (min % 1440) / 60
minutes = min % 60  
print("입력한 분은  일 : %d, 시간 : %d , 분 : %d " %(day, hour, minutes))