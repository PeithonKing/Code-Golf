d=input
def i():return map(int,d().split())
for _ in range(int(d())):
 N,K,E,M=i()
 g = [sum(i()) for _ in range(N)]
 a=sorted(g[:-1])[-K]-g[-1]+1
 if a>M:print("Impossible")
 elif a<0:print(0)
 else:print(a)