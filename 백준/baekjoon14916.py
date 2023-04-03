#백준 14916번 거스름돈
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

while n > 0:  
  if n == 1 or n == 3:
    cnt = -1
    break
  elif n % 5 ==0:  
    n = n - 5
    cnt += 1
  elif (n-5)%2 == 0:
    n = n - 5
    cnt +=1
  elif n % 2 == 0:
    n = n - 2
    cnt +=1

print(cnt)