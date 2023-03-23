#백준 1874번 스택수열
import sys
input = sys.stdin.readline

cnt = 1
flag = 0
stack = []
ans = []

N = int(input().rstrip())

for i in range(N):
  num = int(input())
  while cnt <= num:
    stack.append(cnt)
    ans.append("+")
    cnt += 1

  if stack[-1] == num:
    stack.pop()
    ans.append("-")
  else:
    flag = 1
    break

if flag == 1:
  print("NO")
else:
  for i in ans:
    print(i)
