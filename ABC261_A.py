import io
import sys

_INPUT = """\
6
0 3 1 5
0 1 4 5
0 3 3 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  L1,R1,L2,R2=map(int,input().split())
  if R1<=L2 or R2<=L1: print(0)
  else: print(min(R1,R2)-max(L1,L2))