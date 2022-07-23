import io
import sys

_INPUT = """\
6
5
1 5 2 2 1
3 2 1 2 1
3
1 1 1
3 2 1
3
3 1 2
1 1 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  class BIT:
      def __init__(self, n):
          self._n = n
          self.data = [0] * n
      def add(self, p, x):
          assert 0 <= p < self._n
          p += 1
          while p <= self._n:
              self.data[p - 1] += x
              p += p & -p
      #合計にはrを含まない
      def sum(self, l, r):
          assert 0 <= l <= r <= self._n
          return self._sum(r) - self._sum(l)
      def _sum(self, r):
          s = 0
          while r > 0:
              s += self.data[r - 1]
              r -= r & -r
          return s

  N=int(input())
  C=list(map(int,input().split()))
  X=list(map(int,input().split()))
  tmp=[(C[i],X[i],i) for i in range(N)]
  tmp.sort(key=lambda x: (x[1],x[2]))
  tmp=[(tmp[i][0],tmp[i][2]) for i in range(N)]
  bit=BIT(N)
  ans=0
  for i in range(N):
    ans+=bit.sum(tmp[i][1],N)
    bit.add(tmp[i][1],1)
  from collections import defaultdict
  d=defaultdict(list)
  for i in range(N):
    d[tmp[i][0]].append(tmp[i][1])
  for k in d:
    s=d[k]
    tmp=[(s[i],i) for i in range(len(s))]
    tmp.sort()
    s=[tmp[i][1] for i in range(len(s))]
    bit=BIT(len(s))
    for i in range(len(s)):
      ans-=bit.sum(s[i],len(s))
      bit.add(s[i],1)
  print(ans)