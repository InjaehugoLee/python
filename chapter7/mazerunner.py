# 미로 찾기 
# [0,0]이 입구, [n-1, n-1]이 출구
# 0은 통로, 1은 벽, 이동은 상하좌우만 가능
# 입구에서 출구까지의 탈출 경로를 찾으시오.

# Stack 이라는 클래스를 만들어서 시작점, 푸시, 팝, 사이즈, 프린트 함수
class Stack:
    def __init__(self):
        self.L=[]
    # 미로를 계속 이동
    def push(self, data):
        self.L.append(data)
    # 미로에 막혔을 때, pop
    def pop(self):
        return self.L.pop() 


# 미로 크기 및 형태 설정 (0은 통로, 1은 벽)
msize = 8
m = [[0,0,0,0,0,0,0,1], 
    [0,1,1,0,1,1,0,1],
    [0,0,0,1,0,0,0,1],
    [0,1,0,0,1,1,0,0],
    [0,1,1,1,0,0,1,1],
    [0,1,0,0,0,1,0,1],
    [0,0,0,1,0,0,0,1],
    [0,1,1,1,0,1,0,0]]   

y=0
x=0
m[y][x]=2
s=Stack()

while 1:
    if x<7 and m[y][x+1]==0:
        s.push((y,x))
        x+=1
        m[y][x]=2

    elif y>0 and m[y-1][x]==0:
        s.push((y,x))
        y-=1
        m[y][x]=2

    elif x>0 and m[y][x-1]==0:
        s.push((y,x))
        x-=1
        m[y][x]=2

    elif y<7 and m[y+1][x]==0:
        s.push((y,x))
        y+=1
        m[y][x]=2

    else:
        p=s.pop()
        print(p)
        
        y=p[0]
        x=p[1]
        
    if m[7][7]==2:
        s.push((y,x))
        break

print(s.L)
        
