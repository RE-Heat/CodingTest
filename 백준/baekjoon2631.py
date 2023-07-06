#백준 2631 줄 세우기
import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(1, N + 1):
  mx = 0
  for j in range(0, N):
    if lst[i] > lst[j]:
      mx = max(mx, dp[j])
  dp[i] = mx + 1

print(N - max(dp))
