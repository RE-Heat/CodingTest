#백준 1748번 수 이어 쓰기
import sys
input = sys.stdin.readline

n = int(input())
a = 0

for i in range(1, len(str(n))+1):
  a += 9 * (10 ** (i-1)) * i

b = (10 ** len(str(n)) - n - 1) * len(str(n))
print(a-b)
  
#시간초과
# n = int(input())
# ans = 0
# sum = 1

# for i in range(1, n+1):  
#   if i < 10 ** len(str(i)):        
#     ans += len(str(i))

# print(ans)