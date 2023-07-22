#백준 5557 1학년
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N-1)]
dp[0][arr[0]] = 1

for i in range(1, N-1):
  for j in range(21):
    if dp[i-1][j] !=0:
      pre_value = j
      next_value = arr[i]
      #덧셈
      if 0<=pre_value + next_value <=20:
        dp[i][pre_value + next_value] += dp[i-1][pre_value]
      #뺄셈
      if 0<=pre_value - next_value <=20:
        dp[i][pre_value - next_value] += dp[i-1][pre_value]

for i in dp:
  print(i)
print(dp[N-2][arr[-1]])