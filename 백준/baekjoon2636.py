#백준 2636번 치즈
import sys
from collections import deque
input = sys.stdin.readline

X, Y = map(int, input().split())
cheeze = []
cnt = 0

for i in range(X):
  cheeze.append(list(map(int, input().split())))
  cnt += sum(cheeze[i]) #치즈 전체 개수
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque([(0, 0)])
  melt = deque([])
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<X and 0<=ny<Y and not visited[nx][ny]:
        visited[nx][ny] = 1
        #공기일 때
        if cheeze[nx][ny] == 0:
          q.append((nx, ny))
        #치즈일 때
        if cheeze[nx][ny] == 1:
          melt.append((nx, ny))
  #치즈 녹이기
  for x, y in melt:
    cheeze[x][y] = 0
  return len(melt) #녹인 치즈 개수 리턴

time = 1

while True:
  visited = [[0] * Y for _ in range(X)]
  meltedCnt = bfs()
  cnt -= meltedCnt
  if cnt == 0: #전체 치즈가 다 녹았으면
    print(time, meltedCnt, sep="\n")
    break
  time+=1