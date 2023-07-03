#백준 17070 파이프 옮기기
import sys
input = sys.stdin.readline

def dfs(x, y, type): #0가로 1세로 2대각선
  global cnt
  #(N,N)도달
  if x == n-1 and y == n-1:
    cnt+=1
    return
  #가로 
  if type == 0 or type == 2:
    if y+1 < n and board[x][y+1] == 0:
      dfs(x, y+1, 0)
  #세로
  if type == 1 or type == 2:
    if x+1 < n and board[x+1][y] == 0:
      dfs(x+1, y, 1)
  #대각선
  if type == 0 or type == 1 or type == 2:
    if x+1 < n and y+1 <n:
      if board[x][y+1] == 0 and board[x+1][y] == 0 and board[x+1][y+1] == 0:
        dfs(x+1, y+1, 2)
  

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dfs(0, 1, 0)
print(cnt)