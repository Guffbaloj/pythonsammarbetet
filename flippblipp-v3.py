def flippBlipp(num):
    if num % 15 == 0:
        return "flipp blipp"

    elif num % 3 == 0:
        return "flipp"

    elif num % 5 == 0:
        return "blipp"
    
    else: 
        return str(num)
    
def playFlippBlipp(currentNum):    
    playerAwnser = input("")
    correctAwnser = flippBlipp(currentNum)

    if playerAwnser == correctAwnser:
        playFlippBlipp(currentNum+1)

    else:
        print(f"FEL - {correctAwnser} \nGame Over")



#här körs det
print("Vi ska köra Flipp, Blipp!\n Du kan reglerna, så nu kör vi!!!")
print("1")
playFlippBlipp(2)