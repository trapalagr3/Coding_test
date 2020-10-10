## 내가 작성한 코드 ##
n,k = map(int,input().split())
from collections import deque
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
queue = deque([deque([]) for _ in range(k+1)])
for v in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if data[i][j] == v:
                queue[v].append((i,j))
s,x,y = map(int,input().split())
sec,kk = 0,1
def bfs(data,x,y,q):
    dx = [-1,1,0,0]
    dy=[0,0,1,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if not data[nx][ny]:
            data[nx][ny] = data[x][y]
            q.append((nx,ny))
    return data

while True:
    if sec == s:
        break
    for kk in range(1,k+1):
        qx,qy = queue[kk].popleft()
        temp = bfs(data,qx,qy,queue[kk])
    sec+=1

# 결과 출력
print(temp[x-1][y-1])

## 정답 코드 ##

from collections import deque

n,k = map(int,input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int,input().split())))
    for j in range()
