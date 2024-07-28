import sys
from collections import deque
input = sys.stdin.readline

s = int(input())

def bfs(len_init):
    q = deque([(len_init, len_init)])

    result = 1
    while q:
        sz = len(q)
        for _ in range(sz):
            screen, clipboard = q.popleft()
            if screen == s:
                return result

            # paste character in clipboard to screen
            q.append((screen + clipboard, clipboard))

            # delete one character in screen
            q.append((screen - 1, clipboard))

            # copy all characters in screen to clipboard
            q.append((screen, screen))

        result += 1

    return 0

print(bfs(1))