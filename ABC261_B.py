import io
import sys

_INPUT = """\
6
4
-WWW
L-DD
LD-W
LDW-
2
-D
D-
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=[input() for _ in range(N)]
  ans='correct'
  for i in range(N):
    for j in range(N):
      if i==j: continue
      if A[i][j]=='W' and A[j][i]!='L': ans='incorrect'
      if A[i][j]=='L' and A[j][i]!='W': ans='incorrect'
      if A[i][j]=='D' and A[j][i]!='D': ans='incorrect'
  print(ans)