#백준 9095 1, 2, 3 더하기
import sys
input = sys.stdin.readline

dp = [0] * 1000000

def dpPlus(num):
  if num == 1:
    return 1
  elif num == 2:
    return 2
  elif num == 3:
    return 4

  if dp[num] != 0:
    return dp[num]
  else:
    dp[num] = dpPlus(num - 1) + dpPlus(num - 2) + dpPlus(num - 3)
    return dp[num]

n = int(input())

for i in range(n):
  num = int(input())
  print(dpPlus(num))
