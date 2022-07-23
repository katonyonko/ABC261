import io
import sys

_INPUT = """\
6
3 10
3 3
2 5
1 12
9 12
1 1
2 2
3 3
1 4
2 5
3 6
1 7
2 8
3 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def change(k,o):
    if o==0: return 0
    elif o==1: return 1
    elif o==2: return k
    else: return (k+1)%2
  N,C=map(int,input().split())
  ans=[1 if (C>>i)&1==1 else 0 for i in range(30)]
  ope=[2]*30 #0にする、1にする、不変、変更する
  for _ in range(N):
    T,A=map(int,input().split())
    for i in range(30):
      if T==1 and (A>>i)&1==0: ope[i]=0
      if T==2 and (A>>i)&1==1: ope[i]=1
      if T==3 and (A>>i)&1==1:
        if ope[i]==0: ope[i]=1
        elif ope[i]==1: ope[i]=0
        elif ope[i]==2: ope[i]=3
        else: ope[i]=2
    ans=[change(ans[i],ope[i]) for i in range(30)]
    print(sum([ans[i]<<i for i in range(30)]))