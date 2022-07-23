import io
import sys

_INPUT = """\
6
7 6 1
1 2 1
1 3 10
2 4 100
2 5 102
3 6 20
3 7 30
3 6 3
1 2 1
2 1 2
2 3 3
3 2 4
3 1 5
1 3 6
4 4 1
1 2 1
2 3 1
3 1 1
2 4 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  N,M,v=map(int,input().split())
  G=[set() for _ in range(N)]
  G2=[[] for _ in range(N)]
  for i in range(M):
    A,B,C=map(int,input().split())
    A-=1; B-=1
    G[A].add((C,B))
    G2[B].append((C,A))
  d=deque([])
  ans=[[10**20,0] for _ in range(N)]
  for i in range(N):
    if len(G[i])==0:
      d.append(i)
      ans[i][0]=0
  while d:
    x=d.popleft()
    for c,k in G2[x]:
      ans[k][0]=min(ans[k][0],ans[x][1]+c)
      ans[k][1]=max(ans[k][1],ans[x][0]+c)
      G[k].remove((c,x))
      if len(G[k])==0: d.append(k)
  if ans[v-1][0]==10**20: print('INFINITY',ans)
  else: print(ans[v-1][0])