E, S, M = map(int, input().split())

a = 1
b = 1
c = 1
year = 1

while True:
    if a == E and b == S and c == M:
        print(year)
        break
    
    else:
        a += 1
        b += 1
        c += 1
        
        if a == 16:
            a = 1
        if b == 29:
            b = 1
        if c == 20:
            c = 1
        year += 1