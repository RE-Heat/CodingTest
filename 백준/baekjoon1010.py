#백준 1010번 다리놓기
#itertools combinations는 시간초과
import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  combi = math.comb(m, n)
  print(combi)
