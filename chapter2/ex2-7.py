# 1부터 n까지의 합은 n(n+1)/2로 주어진다. 1부터 100까지의 합을 구하여 출력하는 프로그램
sum = int(input("1부터 n까지의 합을 구하는 프로그램. n을 입력하세요."))
result = sum*(sum+1)/2
print("값은 : %d" %result)