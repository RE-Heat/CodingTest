#백준 1463번 : 1로 만들기
import sys
input = sys.stdin.readline

x = int(input())
dp = [0] * (x + 1)

#1은 0이므로 2부터 시작
for i in range(2, x + 1):
  #하나 빼기 기본값으로 설정
  dp[i] = dp[i - 1] + 1

  #2로 나눌 때 횟수
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i // 2] + 1)

  #3으로 나눌 때 횟수
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[x])
