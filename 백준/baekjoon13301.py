#백준 13301번 타일 장식물
import sys
input = sys.stdin.readline

n = int(input())
dp= {}
round = {}

def fibo(num):
  if num in dp:
    return dp[num]
  
  if num == 1:
    dp[1]= 1
    round[1] = 4
    return 1
  elif num ==2:
    dp[2] = 1
    round[2] = 6
    return 1
  else:
    dp[num] = fibo(num-2) + fibo(num-1)
    round[num] = 2*dp[num] + round[num-1]
    return dp[num]

fibo(n)
print(round[n])