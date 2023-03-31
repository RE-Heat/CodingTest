#백준 2579번 계단오르기
import sys
input = sys.stdin.readline

n = int(input())
score = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(n):
  score[i] = int(input())
  dp[0] = score[0]
  dp[1] = score[0] + score[1]
  dp[2] = max(score[0]+score[2], score[1]+score[2])

for j in range(3, n):
  dp[j] = max(dp[j-2] + score[j], dp[j-3] + score[j-1] + score[j])

print(dp[n-1])