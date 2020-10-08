from collections import deque

# N,M을 공백으로 구분하여 입력받기
n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
    queue =deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 미로 찾기 공간을 벗어난 경우 무시
        if nx < 0 or ny <0 or nx>=n or ny>=m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y]+1
            queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0,0))