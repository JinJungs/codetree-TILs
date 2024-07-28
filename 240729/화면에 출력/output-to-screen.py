import sys
from collections import deque
input = sys.stdin.readline

s = int(input())
visited = [False] * (1001)

def move_list(screen, clipboard):
    l = []
    # paste character in clipboard to screen
    if in_range(screen + clipboard, clipboard):
        l.append((screen + clipboard, clipboard))

    # delete one character in screen
    if in_range(screen -1, clipboard):
        l.append((screen - 1, clipboard))

    # copy all characters in screen to clipboard
    if in_range(screen, screen):
        l.append((screen, screen))

    return l

def in_range(screen, clipboard) -> bool :
    return screen > 0 and screen <= 1000 and clipboard > 0 and clipboard <= 1000

def bfs(len_init :int) -> int:
    q = deque([(len_init, len_init)])

    result = 1
    while q:
        sz = len(q)
        for _ in range(sz):
            screen, clipboard = q.popleft()
            if screen == s:
                return result

            for ns,nc in move_list(screen, clipboard):
                if ns == screen or not visited[ns]:
                    q.append((ns,nc))
                    visited[ns] = True

        result += 1

    return 0

print(bfs(1))