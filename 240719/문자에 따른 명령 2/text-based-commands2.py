import sys
input = sys.stdin.readline

# 기준 dx,dy
d = ['E','S','W','N']
dx = [1,0,-1,0]
dy = [0,-1,0,1]

# 현재값
x,y = 0,0
dir_index = 3 # north

for command in input():
    if command == 'F':
        x += dx[dir_index]
    elif command == 'L':
        dir_index = dir_index-1 if dir_index > 0 else 3
    elif command == 'R':
        dir_index = dir_index+1 if dir_index < 3 else 0

print(x,y)