#백준 13305번 주유소
#break 깜빡해서 조금 헤맴

import sys
input = sys.stdin.readline

N = int(input())  
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

cost = distance[0] * price[0]
min_cost = price[0]

for i in range(N-1):
  if(min_cost<=price[i]):
    cost += min_cost * distance[i]
  else:
    cost += price[i] * distance[i]
    min_cost = price[i]

print(cost)