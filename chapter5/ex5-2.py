# 딕셔너리에 대한 물음에 답하라

d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
#전화번호가 8로 끝나는 사용자 이름을 출력하라
for i in range(0, 4):
    t = d[i].get('phone')
    if t[7]=='8':
        print(d[i].get('name'))
    # if t[7]==8:
    #     print(d[i].get('name'))
# print(d[1].get('phone'))
# print(d[3].get('phone'))

#이메일이 없는 사용자 이름을 출력하라
# for i in range(0, 4):
#     if d[i].get('email')=='':
#         print(d[i].get('name'))

#사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라

# a=input("이름을 입력하세요. 예) Todd, Helga, Princess, LJ")
# for i in range(0, 4):
#     if d[i].get('name')==a:
#         print(d[i].get('phone'))
#         print(d[i].get('email'))
#     else:
#         print("이름이 없습니다.")
#         break