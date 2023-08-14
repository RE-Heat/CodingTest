#백준 15650번 N과 M (2)
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i+1 for i in range(N)]

for comb in combinations(arr, M):
  print(*comb)