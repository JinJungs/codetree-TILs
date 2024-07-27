import sys
input = sys.stdin.readline

# dfs
def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)

# dfs 함수 호출
dfs(graph, 1, visited)

# 1번 노드를 제외하고 방문한 노드의 개수 출력
count = 0
for v in visited:
    if v:
        count += 1

print(count - 1)