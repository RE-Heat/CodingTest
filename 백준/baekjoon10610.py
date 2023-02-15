#백준 10610번 30

import sys
input = sys.stdin.readline

N = input()
str = list(N)
str.pop()
str.sort(reverse=True)

data=""

for i in range(len(str)):
  data = data + str[i]

if '0' not in str or int(data)%3!=0:
  print(-1)
elif int(data)%3==0:
  print(data)