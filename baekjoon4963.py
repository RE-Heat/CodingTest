#백준 4963번 섬의 개수
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dire = [(1, 0), (0, 1), (1, 1), (-1, 0), (0,-1), (-1, -1), (1, -1), (-1, 1)]

def traverse(matrix, i, j):
  if matrix[i][j] == 0:
    return
  matrix[i][j] = 0
  for d in dire:
    ny = i + d[0]
    nx = j + d[1]
    if nx < 0 or ny < 0 or nx >=x or ny >=y:
      continue
    if matrix[ny][nx] == 1:
      traverse(matrix, ny, nx)  

def countIsland(x, y, matrix):
  count = 0
  for i in range(y):
    for j in range(x):
      if matrix[i][j] == 1:
        count +=1
        traverse(matrix, i, j)
  return count  

while True:
  xandy = input()
  x, y = map(int, xandy.split())
  if x == 0 and y == 0:
    break
  matrix = [list(map(int, input().split())) for _ in range(y)]
  print(countIsland(x, y, matrix))
