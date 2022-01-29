p, i, d = print, input, int
def h(x, y):
 a, b = x, y
 while(y):x,y=y,x%y
 return d(a*b/x)
for _ in range(d(i())):
 n,a,b,k=map(d,i().split())
 if n//a+n//b-2*(n//h(a,b))<k:p("Lose")
 else:p("Win")