#백준 11047번 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
ans = 0
for _ in range(N):
  coins.append(int(input()))

for coin in reversed(coins):
  if (K // coin) != 0:
    ans += K // coin
    K -= coin * (K // coin)

print(ans)
