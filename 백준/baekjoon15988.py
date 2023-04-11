#백준 15988번 1, 2, 3 더하기 3
import sys
input = sys.stdin.readline

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
  dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

t = int(input())
for _ in range(t):
  n = int(input())
  print(dp[n])

#피보나치 방법 실패
# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# t = int(input())
# dp = [0] * 1000001
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4

# def cal(num):
#   if dp[num]!=0:
#     return dp[num]
  
#   if num == 1:
#     return dp[1]
#   elif num == 2:
#     return dp[2]
#   elif num == 3:
#     return dp[3]
#   else:
#     dp[num] = (cal(num-3) + cal(num-2) + cal(num-1)) % 1000000009
#     return dp[num]

# for _ in range(t):
#   n = int(input())
#   print(cal(n))

# #큐 찾기
# import sys
# from collections import deque
# input = sys.stdin.readline

# t = int(input())
# queue = deque([1, 2, 4])

# for _ in range(t):
#   n = int(input())
#   if n == 1 or n == 2:
#     print(print(n))
#   elif n == 3:
#     print(4)
#   elif n == 4:
#     print(7)
#   else:
#     for i in range(n - 4):
#       queue.append(sum(queue))
#       queue.popleft()      
#     print(sum(queue) % 1000000009)
#     queue.clear()
#     queue = deque([1, 2, 4]) 