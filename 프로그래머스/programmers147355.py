#프로그래머스 크기가 작은 부분문자열

#내 풀이
def solution(t, p):
  answer = 0
  for i in range(len(t) - len(p) + 1):
    if t[i:i + len(p)] <= p:
      answer += 1
  return answer

#다른 사람 풀이 (동일함)