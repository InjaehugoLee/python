# break 문

n=10
while n >= -10:
    if n == 0:
        break # n = 0 이면 while 블록을 빠져나온다
    inv = 1.0 / n
    print(inv)
    n = n-1