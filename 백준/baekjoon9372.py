#백준 9372번 상근이의 여행
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  for _ in range(m):
    a, b = map(int, input().split())
  print(n-1)

#DFS 적용시
def dfs(node, cnt):
    V[node] = 1
    
    for adj_node in graph[node]:
        if V[adj_node] == 0:
            cnt = dfs(adj_node, cnt+1)
    
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    V = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(dfs(1, 0))