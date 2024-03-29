#백준 10828번 스택
import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
  cmd = list(input().split())
  if cmd[0] == 'push':
    stack.append(cmd[1])
  elif cmd[0] == 'top':
    if not stack:
      print(-1)
    else:
      print(stack[-1])
  elif cmd[0] == 'size':
    print(len(stack))
  elif cmd[0] == 'empty':
    if not stack:
      print(1)
    else:
      print(0)
  elif cmd[0] == 'pop':
    if not stack:
      print(-1)
    else:
      print(stack.pop())
