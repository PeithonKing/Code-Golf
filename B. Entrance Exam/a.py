# code for Code-chef problem "Entrance exam"
r = range
for _ in range(int(input())):
    N, K, E, M = map(int, input().split())
    marks = [[]]*N
    for i in range(N-1):
         