#백준 11651번 좌표 정렬하기2

import sys
input = sys.stdin.readline

N = int(input())
arr = []

#버전 1
for _ in range(N):
  xy = list(map(int, input().split()))
  arr.append([xy[1], xy[0]])

arr.sort()

for i in range(N):
  print(arr[i][1], arr[i][0])

#버전 2 (람다함수 활용)
for _ in range(N):
  arr.append(list(map(int, input().split())))

arr.sort()
arr.sort(key=lambda x: x[1])

for a in arr:
  print(*a)

#버전 3 (람다함수 풀어쓰기)
def my_key(x):
  return x[1]

arr2 = sorted(arr, key=my_key)

for b in arr2:
  print(*b)
