import sys
input = sys.stdin.readline

x,y = 0,0
d = ['E','S','W','N']
dx = [1,0,-1,0]
dy = [0,-1,0,1]

n = int(input())
for _ in range(n):
    direction, distance = input().split()
    for i in range(4):
        if d[i] == direction:
            x += dx[i] * int(distance)
            y += dy[i] * int(distance)
            break

print(str(x) + ' ' + str(y))