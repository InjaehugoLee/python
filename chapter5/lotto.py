import random
pick = set() # 빈 집합
while len(pick) < 6:
    n = random.randint(1,45)
    if n not in pick:
        pick.add(n)
print(pick)
print(sorted(pick))