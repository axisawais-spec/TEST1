secret=27
attempts=5
while attempts<=5:
    guess = int(input("tell a number 1-50"))
    attempts += 1

    if guess==secret:
        print("you win")
    else:
        range=(guess-secret)
        if range<5:
            print("hot")
        if range<10:
            print("warm")
        if range<20:
            print("cold")
        else:
            print("ice cold")
