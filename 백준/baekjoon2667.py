#백준 2667번 단지번호붙이기
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = []
ans = []
cnt = 0

for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  global cnt
  
  if x < 0 or x >=n or y<0 or y>=n:
    return
    
  if graph[x][y] == 1:
    cnt +=1
    graph[x][y] = 0
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]   
      dfs(nx, ny)

for i in range(n):
  for j in range(n):
    if graph[i][j] == '1':
      dfs(i, j)
      ans.append(cnt)
      cnt = 0
      
ans.sort()

print(len(ans)) 
for k in ans: 
  print(k)
