#백준 2847번 게임을 만든 동준이

import sys
input = sys.stdin.readline

N = int(input())

arr=[]

for _ in range(N):
  arr.append(int(input()))

arr.reverse()
cnt = 0

for i in range(N-1):  
  first = arr[i]
  second = arr[i+1]
  
  if(first<=second):
    cnt = cnt + second - (first-1)
    arr[i+1] = first-1    

print(cnt)

