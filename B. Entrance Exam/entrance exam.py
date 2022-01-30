i=lambda:map(int,input().split())
for _ in range(int(input())):
 N,K,E,M=i()
 g=[sum(i())for _ in range(N)]
 a=sorted(g[:-1])[-K]-g[-1]+1
 print("Impossible"if a>M else max(0,a))