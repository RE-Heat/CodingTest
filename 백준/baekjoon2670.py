#백준 2670번 : 연속부분최대곱
import sys
input = sys.stdin.readline

n = int(input())
dp = [float(input()) for i in range(n)]

for i in range(1, n):
  dp[i] = max(dp[i] * dp[i - 1], dp[i])

print("%.3f" % round(max(dp), 3))
