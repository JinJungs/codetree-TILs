import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

def near(grid, x, y):    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    n_list = []

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and grid[nx][ny] == 1:
            n_list.append((nx,ny))

    return n_list

def bfs(grid, fsx, fsy, visited):
    queue = deque([(fsx, fsy)])
    visited[fsx][fsy] = True

    distance = 0
    while queue:
        # queue 사이즈를 체크 - 큐의 사이즈는 변하므로 따로 변수로 빼기
        sz = len(queue)
        for z in range(sz):
            x, y = queue.popleft()
            # print(x, y)
            if x == n-1 and y == m-1:
                return distance
                break

            # 인접한 좌표를 방문처리
            for nx,ny in near(grid, x, y):
                if not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = True    

        # 큐 사이즈만큼 돌고나면 거리 + 1
        distance += 1

    return 0

# bfs 시작
result = bfs(grid, 0, 0, visited)
print(result)