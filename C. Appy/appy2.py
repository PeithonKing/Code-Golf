def hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y): 
    return int(x*y/hcf(x, y))

for _ in range(int(input())):
    inp = input()
    n, a, b, k = [int(i) for i in inp.split(" ")]
    
    first = n // a
    sec = n // b
    third = n // lcm(a, b)

    l = first + sec - 2*third
    if l < k: 
        print("Lose")
    else:
        print("Win")