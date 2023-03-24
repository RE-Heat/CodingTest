#백준 11723번 집합
import sys

input = sys.stdin.readline

S = set()
N = int(input())

for _ in range(N):
  cmd = list(map(str, input().split()))

  if len(cmd) == 1:
    if cmd[0] == 'all':
      S = set([i for i in range(1, 21)])
    else:
      S = set()
    continue

    command = cmd[0]
    val = int(cmd[1])

  if command == 'add':
    S.add(val)
  elif command == 'remove':
    S.discard(val)
  elif command == 'toggle':
    if val in S: S.discard(val)
    else: S.add(val)
  elif command == 'check':
    print(1 if val in S else 0)
