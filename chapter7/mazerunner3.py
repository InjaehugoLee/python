class Queue :
    def __init__(self):
        self.L=[]
    def push(self, data):
        self.L.append(data)
    def pop(self):
        t = self.L[0]
        self.L = self.L[1:]
        return t
    def size(self):
        return len(self.L)
    def printQueue(self):
        for t in self.L:print(t)

# MZSIZE=8 # maze size
# maze = [
#     [0,0,0,0,0,0,0,1],
#     [0,1,1,0,1,1,0,1],
#     [0,0,0,1,0,0,0,1],
#     [0,1,0,0,1,1,0,0],
#     [0,1,1,1,0,0,1,1],
#     [0,1,0,0,0,1,0,1],
#     [0,0,0,1,0,0,0,1],
#     [0,1,1,1,0,1,0,0]
# ]

MZSIZE=16 # maze size
maze = [
    [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
    [0,1,1,0, 1,0,1,1, 1,1,1,0, 1,0,1,0],
    [0,0,1,0, 0,0,0,0, 0,0,1,0, 1,0,1,1],
    [1,0,1,1, 1,1,1,1, 1,0,1,0, 0,0,1,0],
    [0,0,0,0, 0,0,0,1, 0,0,1,1, 1,0,1,0],
    [1,0,1,1, 1,1,0,1, 1,1,1,0, 0,0,0,0],
    [0,0,0,0, 0,0,0,0, 0,0,1,1, 1,1,1,1],
    [0,1,1,1, 0,1,1,1, 1,0,0,1, 0,0,0,1],
    [0,0,0,0, 0,0,0,0, 1,1,1,1, 0,1,0,0],
    [1,1,0,1, 1,1,1,0, 0,1,0,1, 0,1,1,0],
    [0,0,0,1, 0,1,1,1, 0,0,0,1, 0,1,0,0],
    [0,1,1,1, 0,0,0,1, 1,1,1,1, 0,1,0,1],
    [0,1,0,0, 0,1,0,0, 1,0,1,1, 0,1,0,1],
    [0,0,0,1, 1,1,1,0, 1,0,0,0, 0,1,0,0],
    [1,0,1,1, 0,0,1,0, 1,1,1,0, 1,1,1,0],
    [0,0,0,0, 0,1,1,0, 0,0,0,0, 0,0,1,0]
]

# 현재 위치에서 방문할 수 있는 위치를 리스트로 반환
def getNextPos(pos):   # pos ==> (0,0)
    # 새로운 좌표를 계산할 데이터
    val = [[0,1],[-1,0],[0,-1],[1,0]] # 3시,12시,9시,6시
    ret = []
    for t in val:
        # 조사할 새로운 위치의 좌표를 계산
        row = pos[0]+t[0]
        col = pos[1]+t[1]
        # 미로 범위를 벗어나면
        if MZSIZE <= row or MZSIZE <= col or row < 0 or col < 0 :
            continue
        # 새로운 위치가 아직 방문하지 않은 위치라면 ret에 추가
        if maze[row][col] == 0 :
            ret.append((row, col))

    return ret

q=Queue()
pos = (0,0)
maze[0][0] = -1 # 초기화
exitpos = (MZSIZE-1,MZSIZE-1)
bWork = True
extival = 0
while bWork :
    nplist = getNextPos(pos)    # pos로부터 이동할 수 있는 다음 위치를 리스트로 얻는다.
    for np in nplist:
        val = maze[pos[0]][pos[1]]
        maze[np[0]][np[1]] = val-1
        if np == exitpos :
            exitval = val-1
            bWork = False
            break

        q.push(np)

    if q.size() == 0:
        break
    pos = q.pop()

if bWork:
    print("No path!")
else :    
    path=[]
    pos = exitpos
    posval = exitval + 1
    path.append(pos)
    while posval < 0:
        val = [[0,1],[-1,0],[0,-1],[1,0]] # 3시,12시,9시,6시
        for t in val:
            # 조사할 새로운 위치의 좌표를 계산
            row = pos[0]+t[0]
            col = pos[1]+t[1]
            # 미로 범위를 벗어나면
            if MZSIZE <= row or MZSIZE <= col or row < 0 or col < 0 :
                continue

            if maze[row][col] == posval :
                pos = (row, col)
                path.append(pos)
                break
        posval += 1

    print(path)
