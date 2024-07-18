import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

result = 0
for i in range(n):
    for j in range(n):
        count = 0
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if x<0 or x>n-1 or y<0 or y>n-1:
                continue

            if grid[x][y] == 1:
                count +=1

        if count >= 3:
            result += 1

print(result)