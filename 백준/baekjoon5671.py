#백준 5671번 호텔 방 번호
#set()으로 중복 제거 '11' {1} 

import sys
input = sys.stdin.readline

while True:
  data = input().rstrip()
  if not data:
    break
    
  N, M = map(int,data.split())
  ans = 0
  
  for i in range(N, M+1):
    if(len(set(str(i)))==len(str(i))):
      ans +=1
      
  print(ans)