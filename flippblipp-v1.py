def flippblipp(n):
    if n % 3 == 0 and n % 5 == 0:
        return "flippblipp"
    elif n % 3 == 0:
        return "flipp"
    elif n % 5 == 0:
        return "blipp"
    else:
        return n

n = 21

for n in range(1, n+1):
    print(flippblipp(n))