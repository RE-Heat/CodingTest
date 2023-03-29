#백준 11727번 2xn 타일링 2
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dp = [0] * 10000000
n = int(input())


def dynamic(num):
  if num == 1:
    return 1
  elif num == 2:
    return 3

  if dp[num] != 0:
    return dp[num]
  else:
    dp[num] = (dynamic(num - 1) + (2 * dynamic(num - 2))) % 10007
    return dp[num]

print(dynamic(n))