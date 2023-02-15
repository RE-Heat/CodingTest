#백준 1758번 알바생 강호

import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
  arr.append(int(input()))

arr.sort(reverse=True)

sum = 0

for j in range(N):
  if(arr[j]-j>=0):
    sum = sum + (arr[j]-j)
  else:
    break

print(sum)
