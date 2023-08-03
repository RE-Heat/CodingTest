#백준 2251번 물통
import sys
from collections import deque
input = sys.stdin.readline

a, b, c = map(int, input().split())
ans = []

#큐 담기
q = deque()
q.append((0,0))

#방문여부
check = [[False] * (b+1) for _ in range(a+1)]
check[0][0] = True

def pour(x, y):
  if not check[x][y]:
    check[x][y] = True
    q.append((x, y))

def bfs():
  while q:
    #A통에 있는 물 : x, B물통에 있는 물: y, C물통 물 :z
    x, y = q.popleft()
    z = c -x -y

    if x == 0:
      ans.append(z)

    #A->B
    water = min(x, b-y)
    pour(x-water, y+water)    
    #A->C
    water = min(x, c-z)
    pour(x-water, y)
    
    #B->A
    water = min(y, a-x)
    pour(x+ water, y-water)
    #B->C
    water = min(y, c-z)
    pour(x, y-water)

    #C->A
    water = min(z, a-x)
    pour(x+water, y)
    #C->B
    water = min(z, b-y)
    pour(x, y+water)

bfs()
ans.sort()

for i in ans:
  print(i, end=" ")