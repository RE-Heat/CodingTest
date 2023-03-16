#백준 11866번 요세푸스 문제0

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i + 1 for i in range(N)]
arr = deque(arr)
ans = []

#세 번째까지 pop
while arr:
  for _ in range(K - 1):
    arr.append(arr.popleft())
  ans.append(arr.popleft())

print("<", end="")
print(*ans, sep=", ", end=">")
