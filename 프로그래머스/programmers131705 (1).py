#프로그래머스 삼총사
#내 답안
from itertools import combinations

def solution(number):
    answer = 0
    comb = list(combinations(number, 3))
    for i in range(len(comb)):
        if sum(comb[i])==0:
            answer+=1   
    return answer

#다른 답안
#차이점 combinations의 값들을 바로 for문으로 돌렸다.

def solution2(number):
  from itertools import combinations
  answer = 0
  for i in combinations(number,3):
    if sum(i) == 0:
      answer+=1
  return answer

