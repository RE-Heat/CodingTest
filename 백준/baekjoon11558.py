#백준 11558번: The Game of Death
import sys
input = sys.stdin.readline

t = int(input())

def dfs(num):
  for i in graph[num]:
    if pick[i] == 0:
      pick[i] = pick[num] + 1
      dfs(i)

for _ in range(t):
  n = int(input())
  graph = [[] for _ in range(n+1)]
  
  for i in range(1, n+1):
    v = int(input())
    graph[i].append(v)

  pick = [0] * (n+1)  
  dfs(1)  
  print(pick[n]-1 if pick[n]>0 else print(0))