#백준 10989 수 정렬하기3
#메모리 초과

import sys

input = sys.stdin.readline

N = int(input())
num_list = [0] * 100001

for _ in range(N):
  num_list[int(input())] += 1

for i in range(10001):
  if num_list[i] != 0:
    for _ in range(num_list[i]):
      print(i)
