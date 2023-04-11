#백준 9625번 BABBA
import sys
input = sys.stdin.readline

k = int(input())
listA = [0 for _ in range(47)]

def fiboA(num):
  if listA[num] != 0:
    return listA[num]

  if num == 1:
    listA[0] = 0
    return 0
  elif num == 2:
    listA[1] == 1
    return 1
  else:
    listA[num] = fiboA(num - 2) + fiboA(num - 1)
    return listA[num]

print(fiboA(k), fiboA(k + 1))
