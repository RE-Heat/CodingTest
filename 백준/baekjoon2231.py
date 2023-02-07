#백준 2231 분해합

#런타임 에러 뜬 이유 ans = 0 초기화 안 함
n = int(input())
ans = 0

for i in range(n):
  a = list(map(int, str(i)))
  if(i+sum(a)==n):
    ans = i
    break

print(ans)