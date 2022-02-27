for _ in range(int(input())):
    n,k=map(int,input().split())
    q=list(map(int,input().split()))
    a,d=0,0
    while 1:
        try:a+=q[d]-k
        except:a-=k
        print("\t", d, a)
        d+=1
        if a<0:break
    print(d)