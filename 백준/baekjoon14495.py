#백준 14495번 피보나치 비스무리한 수열
import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]

def fibo(num):
  if dp[num]!=0:
    return dp[num]

  if num == 1 or num==2 or num==3:
    return 1
  else:  
    dp[num] = fibo(num-1)+fibo(num-3)
    return dp[num]

print(fibo(n))