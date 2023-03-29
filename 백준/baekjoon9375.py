#백준 9375번 패션왕 신해빈
import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  wear = []
  for _ in range(n):
    item, type = input().split()
    wear.append(type)

  wear_cnt = Counter(wear)
  cnt = 1

  for type in wear_cnt:
    cnt *= wear_cnt[type] + 1

  print(cnt - 1)
