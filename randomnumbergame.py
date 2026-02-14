while True:
    print("WELCOME TO THE NUMBER GUESSING GAME!!!")
    print("I'm guessing a number between 1 to 100,let you guess the correct number")
    
    import random
    sn=random.randint(1,100)
    attempt =0

    while True:
        guess=int(input("guess the number"))
        attempt += 1
    
        if guess<sn:
            print("ohh no, too small try again ")
        elif guess>sn:
            print("too high, try again")
        else:
            print(f"ABSOLUTELY YOU GUESS THE CORRECT NUMBER IN {attempt} ATTEMPTS")
            
            break

    play=input("do you want to play again? (yes/no)").lower()
    if play!="yes":
        print("thanks for playing! bye bye")
        break
