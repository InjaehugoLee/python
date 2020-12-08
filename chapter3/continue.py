# continue 문

n = 10
while n>=-10:
    if n==0: 
        n=n-1
        continue # n=0이면 while 블록의 나머지 부분 건너뜀
    inv = 1.0 / n
    print("n=%d, inv(n) = %0.2f"%(n,inv))
    n=n-1