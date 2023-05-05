#백준 14503번 로봇 청소기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
home_x, home_y, dir = map(int, input().split())

#북0 동1 남 2 서 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]

for _ in range(n):
  graph.append(list(map(int, input().split())))

visited[home_x][home_y] = 1
cnt = 1

while True:
  flag = 0
  #반시계 방향으로 둘러보기
  #북0 서 3 남 2 동 1
  for i in range(4):
    dir = (dir+3) % 4
    nx = home_x + dx[dir]
    ny = home_y + dy[dir]
    
    if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
      if visited[nx][ny] == 0:
        visited[nx][ny] = 1
        cnt +=1
        
        home_x = nx
        home_y = ny
        flag = 1
        break
  #상하좌우가 다 청소돼 후진  
  if flag == 0:
    if graph[home_x-dx[dir]][home_y-dy[dir]]==1:
      print(cnt)
      break
    else:
      home_x = home_x - dx[dir]
      home_y = home_y - dy[dir]