#백준 18870번 좌표 압축
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(set(arr))

dic = {arr2[i]:i for i in range(len(arr2))}

for x in arr:
  print(dic[x], end=" ")