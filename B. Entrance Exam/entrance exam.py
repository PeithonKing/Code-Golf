def i():return map(int,input().split())
def g(a):return [sum(i()) for _ in range(a)]
for _ in range(int(input())):
    N,K,E,M=i()
    a=sorted(g(N-1))[::-1][K-1]-g(1)[0]+1
    if a>M:print("Impossible")
    elif a<0:print(0)
    else:print(a)