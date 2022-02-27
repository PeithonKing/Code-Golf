x = lambda: map(int,input().split())
for _ in range(int(input())):
 n,k=x()
 q=list(x())
 d=1
 while sum(q[:d])-k*d>=0:d+=1
 print(d)