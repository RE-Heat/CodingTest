#백준 1780번 종이의 개수
import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

minus, zero, plus = 0, 0, 0

def paperCnt(x, y, N):
  global minus, zero, plus
  num = paper[x][y]
  for i in range(x, x + N):
    for j in range(y, y + N):
      if paper[i][j] != num:
        next_n = N // 3
        paperCnt(x, y, next_n)
        paperCnt(x + next_n, y, next_n)
        paperCnt(x + next_n * 2, y, next_n)
        paperCnt(x, y + next_n, next_n)
        paperCnt(x + next_n, y + next_n, next_n)
        paperCnt(x + next_n * 2, y + next_n, next_n)
        paperCnt(x, y + next_n * 2, next_n)
        paperCnt(x + next_n, y + next_n * 2, next_n)
        paperCnt(x + next_n * 2, y + next_n * 2, next_n)
        return
  if num == -1:
    minus += 1
  elif num == 0:
    zero += 1
  else:
    plus += 1

paperCnt(0, 0, N)
print(minus)
print(zero)
print(plus)
