#백준 1145번 적어도 대부분의 배수

numbers = list(map(int,input().split()))

ans = 4
max_range = 100000000

#파이썬은 함수로 처리하는 게 더 빠르다.

def cal(numbers):
  for i in range(4, max_range):
    cnt = 0
    for number in numbers:
      if(i % number) == 0:
        cnt+= 1
  
    if cnt >=3:
      return i

print(cal(numbers))

