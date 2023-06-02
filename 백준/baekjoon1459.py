#백준 1459번 걷기
import sys
input = sys.stdin.readline

#가로 세로 시간 W, 가로지르는 시간 S
X, Y, W, S = map(int, input().split())
ans = 0

#평행으로만 이동
ans1 = (X+Y) * W

#대각선으로만 이동, 대각선+평행이동 1번
if (X+Y) % 2 == 0:
  ans2 = max(X,Y) * S
else:
  ans2 = (max(X,Y)-1)*S + W

#대각선 + 평행이동
ans3 = min(X,Y) * S + abs(X-Y) * W

print(min(ans1, ans2, ans3))


# if X==0:
#   ans = min((Y*S+(X-Y)*W), (X+Y)*W, Y*S)
# elif Y ==0:
#   ans = min((Y*S+(X-Y)*W), (X+Y)*W, X*S)
# else:
#   ans = min((Y*S+(X-Y)*W), (X+Y)*W)

# elif X%2 == 1:
#   ans = min((Y*S+(X-Y)*W), (X+Y)*W, Y*S + W)
# elif X%2 == 0:
#   ans = min((Y*S+(X-Y)*W), (X+Y)*W, (Y-1)*S+W)

# print(ans)