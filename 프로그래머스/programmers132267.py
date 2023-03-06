#프로그래머스 콜라 문제

#풀이
def solution2(a, b, n):
  answer = 0
  while (n >= a):
    temp = n % a    
    n = (n // a) * b
    answer = answer + n
    n = n + temp

  return answer

#람다 풀이
solution = lambda a, b, n: max(n - b, 0) // (a - b) * b