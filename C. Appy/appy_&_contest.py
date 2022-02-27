import numpy as p
for _ in range(int(input())):
 n,a,b,k=map(int,input().split())
 print("Lose"if n//a+n//b-2*(n//p.lcm(a,b))<k else"Win")