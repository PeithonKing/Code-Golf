for _ in range(int(input())):
    inp = input()
    b = len(inp)
    if int(inp) != 10**b-1:
        a = list(inp)
        if b % 2 != 0: # odd
            c = int((b - 1) / 2) # mid point
            first_half = "".join(a[:c])
            second_half = "".join(a[c+1:])
            r = a[:c]
            reversed_first_half = "".join(r[::-1])
            
            if int(reversed_first_half) > int(second_half):
                print(first_half + a[c] + reversed_first_half)
            else:
                if a[c] != "9":
                    print(first_half + str(int(a[c]) + 1) + reversed_first_half)
                else:
                    r = str(int(first_half)+1)
                    print(r + "0" + r[::-1])
        else: # even
            c = int(b / 2)
            first_half = "".join(a[:c])
            second_half = "".join(a[c:])
            r = a[:c]
            reversed_first_half = "".join(r[::-1])
            if int(reversed_first_half) > int(second_half):
                print(first_half + reversed_first_half)
            else:
                w = int(first_half) + 1
                print(str(w) + str(w)[::-1])
    else: print(int(inp)+2)