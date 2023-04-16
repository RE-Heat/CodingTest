#백준 18353번 병사 배치하기
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1 for _ in range(n)]

for i in range(1, n):
  for j in range(i):
    if arr[j] < arr[i]:
      print(arr[j], arr[i], dp[i], dp[j]+1)
      dp[i] = max(dp[i], dp[j]+1)

print(len(arr)-max(dp))