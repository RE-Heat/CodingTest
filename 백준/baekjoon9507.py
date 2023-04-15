#백준 9057번 Generations of Tribbles
import sys
input = sys.stdin.readline

dp = [0 for _ in range(68)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

def koong(num):
  if dp[num]!=0:
    return dp[num]
    
  if num < 2:
    return 1
  elif num == 2:
    return 2
  elif num == 3:
    return 4
  else:
    dp[num] = koong(num - 1) + koong(num - 2) + koong(num - 3) + koong(num - 4)
    return dp[num]

t = int(input())
for _ in range(t):
  n = int(input())
  print(koong(n))