#백준 10830번 행렬제곱
import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

#행렬의 곱셈
def mul(U, V):
  n = len(U)
  Z = [[0] * n for _ in range(n)]
  for row in range(n):
    for col in range(n):
      e = 0
      for k in range(n):
        e += U[row][k] * V[k][col]
      Z[row][col] = e % 1000
      
  return Z

#행렬 제곱
def square(A, B):
  n = len(A)
  if B == 1:
    for row in range(n):
      for col in range(n):
        A[row][col] %= 1000
    return A
    
  tmp = square(A, B//2)
  if B % 2 == 1:
    return mul(mul(tmp, tmp), A)
  else:
    return mul(tmp, tmp)

ans = square(A, B)
for i in ans:
  print(*i)