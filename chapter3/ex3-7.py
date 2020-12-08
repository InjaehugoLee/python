# 반복문과 조건문을 사용해 점수를 계속 입력 받아 90점 이상이면 A
# 80점 이상이면 B, 60점 이상이면 C, 40점 이상이면 D
# 39점이하이면 F라고 출력하는 프로그램 작성.
# 입력받은 점수가 음수일 때, 프로그램 종료
score = int(input("점수를 입력하세요"))
while True:
    if score < 0:
        print("점수를 잘못 입력했습니다. 프로그램 종료.")
        break
    elif score >= 90 and score <= 100:
        print("A")
        break
    elif score <90 and score >= 80:
        print("B")
        break
    elif score <80 and score >= 60:
        print("C")
        break
    elif score <60 and score >= 40:
        print("D")
        break
    elif score <40 and score >=0:
        print("F")
        break
    else:
        print("잘못된 점수입니다.")
        break
