# 다음 딕셔너리에 답하라
# days = {'January':31, 'February':28, 'March':31, 'April':30,
# 'May':31, 'June':30, 'July':31, 'August':31,
# 'September':30, 'October':31, 'November':30, 'December':31}

days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}

# 사용자가 월을 입력하면 해당 월에 일수를 출력하라
# day_input=input("월을 입력하세요. ex) January")
# print(days[day_input])

# 알파벳 순서로 모든 월을 출력하라
# days2=list(days.keys())
# days2.sort()
# print(days2)

# 일수가 31인 월을 모두 출력하라
# days3=list(days.values())
# days4=list(days.keys())
# for i in range (0, len(days3)):
#     if days3[i]==31:
#         print(days4[i], end=' ')

# 월의 일수를 기준으로 오름차순으로 (key-value)쌍을 출력하라
# import operator
# sdays = sorted(days.items(), key=operator.itemgetter(1))
# print(sdays)

# ll = days.items()
# tt=[]
# for (k, v) in ll:
#     tt.append((v, k))
# ttt= sorted(tt)
# for v, k in ttt:
#     print(k, v)

# 사용자가 월을 3자리만 입력하면 월의 일수를 출력하라. (Jan, Feb 등)
day_input=input("월을 입력하세요. ex) Jan")
for i in days:
    if i[0:3]==day_input:
        print(days[i])
            break
    