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
    def size(self):
        return len(self.L)
    def printStack(self):
        for t in self.L: print(t) # 리스트 L에 담긴 t를 출력

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

pos=(0,0)
# 다음 번의 위치를 알기 위한 함수(방향 이동)
def getNextPos(pos):    
    # 출구가 있을 경우에 계속 이동
    # 4가지 방향 3시, 12시, 9시, 6시
    Pt=[(0,1),(-1,0),(0,-1),(1,0)]
    for t in Pt:
        r=pos[0]+t[0]
        c=pos[1]+t[1]

        if msize <= r or msize <= c or r < 0 or c <0:
            continue
        if m[r][c]==0:
            return (r,c)

# 클래스 인스턴스화
s=Stack()
exitpos=(msize-1, msize-1)
while True:
    newpos = getNextPos(pos) # pos로부터 다음 위치

    if newpos == exitpos: # 새로운 위치가 출구면 루프 종료
        s.push(pos)
        s.push(newpos)
        break

    elif newpos == None:
        if s.size()==0:
            print("출구가 없습니다.")
            break
        m[pos[0]][pos[1]]=2
        pos = s.pop()
        continue

    else:
        s.push(pos)
        m[pos[0]][pos[1]]=2
        pos = newpos

if s.size() != 0:
    s.printStack()