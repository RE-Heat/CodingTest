#백준 18111번 마인크래프트
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
block = [list(map(int, input().split())) for _ in range(N)]
time = float("inf")
height = 0

for a in range(257):
  add_block = 0
  take_block = 0
  for i in range(N):
    for j in range(M):
      if block[i][j] < a:
        add_block += i - block[i][j]
      else:
        take_block += block[i][j] - i

  if add_block > take_block+B:
    count = add_block + (2 * take_block)

  if time <= count:
    time = count
    height = 1

print(time, height)
  