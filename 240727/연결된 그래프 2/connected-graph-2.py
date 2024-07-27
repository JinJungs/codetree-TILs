import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

def dfs(graph, v, visited):
    # 방문처리
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# n개의 정점에 대해 dfs 처리
counts = [0] * (n+1)
for v in range(1, n+1):
    visited = [False] * (n+1)
    dfs(graph, v, visited)
    counts[v] = sum(visited)

max_count = max(counts)
result = []
for i in range(1, n+1):
    if max_count == counts[i]:
        result.append(str(i))

print(' '.join(result))