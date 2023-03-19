#백준 10773번 제로
import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
zero = deque([])

for _ in range(K):
  n = int(input())
  if n != 0:
    zero.append(n)
  else:
    zero.pop()

print(sum(zero))
