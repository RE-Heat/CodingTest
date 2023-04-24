#백준 25418번 정수 a를 k로 만들기
import sys
input = sys.stdin.readline

a, k = map(int, input().split())
cnt = 0

while True:
  if a == k:
    print(cnt)
    break
  elif k % 2==0 and k >= a*2:
    k = k/2
  else:
    k -= 1
  cnt +=1  
    