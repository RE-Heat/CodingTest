#백준 14002번 가장 긴 증가하는 부분 수열4
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
  mx = 0
  for j in range(i):
    if lst[i] > lst[j]:
      mx = max(mx, dp[j])
  dp[i] = mx + 1

#최장길이 출력
print(max(dp))
x = max(dp)

ans = []
for i in reversed(range(N)):
  if dp[i] == x: #dp[i]값이 최장길이와 같다면
    ans.append(lst[i]) #해당 값 추가
    x -=1 #최장길이 하나씩 감소해서 직전 값 찾기

ans.reverse()
print(*ans)