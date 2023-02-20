#백준 20115번 에너지드링크
#필요없는 '0' 소수점 지우는 법 "g"%

import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int,input().split()))

arr.sort(reverse=True)
sum = arr[0]

for i in range(1, N):
  sum = sum + arr[i]/2

print("g"%sum)
