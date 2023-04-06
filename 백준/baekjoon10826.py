#백준 10826번 : 피보나치 수4
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
dic = {}


def fibo(num):
  if num in dic:
    return dic[num]

  if num == 0:
    dic[0] = 0
    return 0
  elif num == 1:
    dic[1] = 1
    return 1
  else:
    dic[num] = fibo(num - 2) + fibo(num - 1)
    return dic[num]


print(fibo(n))