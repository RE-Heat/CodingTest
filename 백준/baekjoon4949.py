#백준 4949번 균형잡힌 세상
import sys

input = sys.stdin.readline

while True:
  str = input().rstrip()
  if str == ".":
    break

  stack = []

  for a in str:
    if a == "(" or a == "[":
      stack.append(a)
    elif a == ")":
      if stack and stack[-1] == "(":
        stack.pop()
      else:
        stack.append(")")
        break
    elif a == "]":
      if stack and stack[-1] == "[":
        stack.pop()
      else:
        stack.append("]")
        break

  if stack:
    print("no")
  else:
    print("yes")
