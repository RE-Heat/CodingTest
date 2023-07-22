#백준 9663번 N-Queen
import sys
input = sys.stdin.readline

def dfs(n):
  global ans
  if n == N:
    ans += 1
    return
  for i in range(N):
    if v1[i] == v2[n + i] == v3[n - i] == 0:
      v1[i] = v2[n + i] = v3[n - i] = 1
      dfs(n + 1)
      v1[i] = v2[n + i] = v3[n - i] = 0


N = int(input())
ans = 0
v1 = [0] * N
#우상향
v2 = [0] * (2 * N)
#우하향
v3 = [0] * (2 * N)
dfs(0)
print(ans)
