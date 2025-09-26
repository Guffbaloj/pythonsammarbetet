n = 100
def flippBlipp(num):
    if num % 3 == 0 and num % 5 == 0:
        print("flipp", "blipp")

    elif num % 3 == 0:
        print("flipp")

    elif num % 5 == 0:
        print("blipp")
    
    else: 
        print(str(num))

for i in range(1, n+1):
    flippBlipp(i)