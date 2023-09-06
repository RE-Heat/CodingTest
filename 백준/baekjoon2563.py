#백준 2563번 색종이
import sys
input = sys.stdin.readline

N = int(input())
paper = [[0] * 101 for _ in range(101)]

for _ in range(N):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      paper[i][j] = 1

ans = 0
for i in paper:
  ans += i.count(1)

print(ans)