n,k=map(int,input().split())
f=[1]*k+[k]
for i in range(n-k-1):f.append(2*f[-1]-f[i])
print(f[-1]%int(1e9+7) if n>k else 1)