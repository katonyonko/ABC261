import io
import sys

_INPUT = """\
6
6 3
2 7 1 8 2 8
2 10
3 1
5 5
3 2
1000000000 1000000000 1000000000
1 1000000000
3 1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  X=list(map(int,input().split()))
  d=[0]*(N+1)
  for i in range(M):
    C,Y=map(int,input().split())
    d[C]=Y
  dp=[[0]*(N+1) for _ in range(N+1)]
  dp[0][0]=0
  tmp=0
  for i in range(N):
    for j in range(i+2):
      if j==0:
        dp[i+1][j]=tmp
      else:
        dp[i+1][j]=dp[i][j-1]+X[i]+d[j]
    tmp=max(dp[i+1])
  print(max(dp[-1]))