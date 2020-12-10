# 문자 'a'가 들어가는 단어를 키보드에서 입력 받아 첫번째 줄에는 
# 'a'까지 문자열을 출력하고, 두 번째 줄에는 나머지 문자열 출력
word=input("문자열을 입력하세요.")
while True:
    n=word.find('a')
    if n==-1: # find함수를 썼을 때, 못 찾으면 -1을 리턴
        print(word)
        break
    print(word[:n+1])
    word=word[n+1:]