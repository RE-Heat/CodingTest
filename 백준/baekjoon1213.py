#백준 1213번 팰린드롬 만들기
import collections
import sys
input = sys.stdin.readline

str = input().rstrip()
str_count = collections.Counter(str)
flag = 0
ans = ""
mid = ""

#홀수가 2개 이상 나오면 팰린드롬 불가능
for i, j in list(str_count.items()):
  if j % 2 == 1:
    mid = i
    flag +=1    
    if flag >=2 :
      print("I'm Sorry Hansoo")
      exit()

for k, l in sorted(str_count.items()):
  ans += (k * (l//2))

print(ans + mid + ans[::-1])
