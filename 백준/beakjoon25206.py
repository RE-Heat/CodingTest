#백준 25206번 너의 평점은
import sys
input = sys.stdin.readline

rate = 0
creditSum = 0

rating = {
  "A+": 4.5,
  "A0": 4.0,
  "B+": 3.5,
  "B0": 3.0,
  "C+": 2.5,
  "C0": 2.0,
  "D+": 1.5,
  "D0": 1.0,
  "F": 0.0
}

for i in range(20):
  sub, credit, grade = input().split()
  if grade == 'P':
    continue
  rate += float(credit) * rating[grade]
  creditSum += float(credit)

print(rate/creditSum)