import sys
from collections import deque
input = sys.stdin.readline

s = int(input())

def in_range(screen) -> bool :
    return screen > 0 and screen <= s

def bfs(len_init :int) -> int:
    q = deque([(len_init, 0)]) # (screen, clipboard)
    visited = [[False] * (s + 1) for _ in range(s + 1)]
    visited[len_init][0] = True
    result = 0

    while q:
        for _ in range(len(q)):
            screen, clipboard = q.popleft()
            if screen == s:
                return result

            # 1. Copy all characters on the screen to the clipboard
            if not visited[screen][screen]:
                visited[screen][screen] = True
                q.append((screen, screen))


            # 2. Paste characters from the clipboard to the screen
            if clipboard > 0 and in_range(screen + clipboard):
                if not visited[screen + clipboard][clipboard]:
                    visited[screen + clipboard][clipboard] = True
                    q.append((screen + clipboard, clipboard))

            # delete one character in screen
            if in_range(screen - 1):
                if not visited[screen - 1][clipboard]:
                    visited[screen - 1][clipboard] = True
                    q.append((screen - 1, clipboard))


        result += 1

    return result

print(bfs(1))