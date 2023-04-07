#백준 13699번 점화식
import sys
input = sys.stdin.readline

n = int(input())
t = [0] * n

t[0] = 1
t[1] = 1

for i in range(n):
  for j in reversed(range(n)):
    t[i] *= t[j]
    print(t[i])

print(t[n-1])