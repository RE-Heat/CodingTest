#1436번 영화감독 숌

n = int(input())
cnt = 0
num = 0

while True:
  if '666' in str(num):
    cnt += 1
    
  if cnt == n:
    print(num)
    break
    
  num += 1

