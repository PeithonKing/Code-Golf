for _ in range(int(input())):
 n,a,b,k=map(int,input().split())
 for i in range(1,n+1):
  if bool(i%a)!=bool(i%b):k-=1
 print("Lose"if k>0 else"Win")