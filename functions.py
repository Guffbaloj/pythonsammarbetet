def double(n):
    return n * 2

def triple(n):
    return n * 3

def quadruple(n):   
    return double(n) * 2

def funky(n, m):
    return triple(n) + quadruple(m)

a = 5
b = 7

d1  = double(a) # 10
d2  = double(b) # 14

t1  = triple(a) # 15
t2  = triple(b) # 21

q1  = quadruple(a) # 20
q2  = quadruple(b) # 28

f1  = funky(a, b) # 43
f2  = funky(b, b) # 49

print(d1, d2, t1, t2, q1, q2, f1, f2)