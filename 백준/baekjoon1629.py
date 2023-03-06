#백준 1629번 곱셈
# 0.5초

import sys
input = sys.stdin.readline

def multiply(A, B, C):
  if B == 1:
    return A % C
  elif B % 2 == 0:
    return (multiply(A, B // 2, C)**2) % C
  elif B % 2 == 1:
    return ((multiply(A, B // 2, C)**2) * A) % C

A, B, C = map(int, input().split())

print(multiply(A, B, C))