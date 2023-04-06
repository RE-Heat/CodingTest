#백준 10211번 Maximum subarray
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))

  for i in range(1, n):
    arr[i] = max(arr[i] + arr[i - 1], arr[i])

  print(max(arr))