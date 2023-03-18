#백준 11650번 좌표 정렬하기
import sys

input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
  arr.append(list(map(int, input().split())))

arr.sort()
for a in arr:
  print(*a)
