#백준 14888번 연산자 끼워넣기
import sys
input = sys.stdin.readline

#DFS 활용
N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9

def dfs(depth, val):
  global add, sub, mul, div, max_val, min_val
  if depth == N:
    max_val = max(max_val, val)
    min_val = min(min_val, val)
  else:
    #더하기
    if add > 0:
      add -= 1
      dfs(depth + 1, val + num[depth])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(depth + 1, val - num[depth])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(depth + 1, val * num[depth])
      mul += 1
    if div > 0:
      div -= 1
      dfs(depth + 1, val / num[depth])
      div += 1

dfs(1, num[0])
print(max_val)
print(min_val)
