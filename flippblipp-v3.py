def flippblipp(n):
    if n % 3 == 0 and n % 5 == 0:
        return("flipp blipp")
    elif n % 3 == 0:
        return("flipp")
    elif n % 5 == 0:
        return("blipp")
    else:
        return(n)

n = 1
print(flippblipp(n))

while True:
    n += 1
    i = (input("Nästa "))
    if i == str(flippblipp(n)):
        continue
    else:
        print("Fel -", flippblipp(n))
        print("Game over")
        break