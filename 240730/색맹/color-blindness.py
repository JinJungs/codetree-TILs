import sys

n = int(input())
normal_grid = [list(input()) for _ in range(n)]
color_blind_grid = [['R' if cell == 'G' else cell for cell in row] for row in normal_grid]
normal_visited = [[False] * n for _ in range(n)]
color_blind_visited = [[False] * n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def in_range(x,y) -> bool:
    return x >= 0 and y>=0 and x<n and y<n

# how to distinguish between the first time of the block and the end of it?
# for loop should be inside of it
def dfs(grid, x, y, visited):
    visited[x][y] = True
    result = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx,ny) and not visited[nx][ny] and grid[x][y] == grid[nx][ny] :
            result += dfs(grid, nx, ny, visited)
    return result

def loop_dfs(grid, visited) -> int:
    district = []
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                district.append(dfs(grid, x, y, visited))
    return len(district)


print(loop_dfs(normal_grid, normal_visited), end=' ')
print(loop_dfs(color_blind_grid, color_blind_visited))