import io
import sys

_INPUT = """\
6
5
newfile
newfile
newfolder
newfile
newfolder
11
a
a
a
a
a
a
a
a
a
a
a
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  d=dict()
  for i in range(N):
    S=input()
    if S in d:
      print(S+'(',d[S],')',sep='')
      d[S]+=1
    else:
      print(S)
      d[S]=1