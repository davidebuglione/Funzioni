def print_n(t, n = 1, u = False):
    if u == True:
        t = t.upper()
        
    for i in range(n):
        print(t, end = " ")

print_n("ciao", 10, u = True)

def differenza(a, b):
    return a - b

c = differenza(4, 2)
