import sys

n = int(input())
li = []

for _ in range(9):
    commands = list(input().split())
    command = commands[0]
    if len(commands) == 2:
        num = int(commands[1])

    if command == 'push_back':
        li.append(num)
    elif command == 'pop_back':
        li.pop()
    elif command == 'size':
        print(len(li))
    elif command == 'get':
        print(li[num-1])