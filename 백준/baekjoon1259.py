#백준 1259번 팰린드롬수
import sys

input = sys.stdin.readline

while True:
  str = input()
  reverseStr = str[::-1]

  if int(str) == 0:
    break

  if int(str) == int(reverseStr):
    print("yes")
  else:
    print("no")