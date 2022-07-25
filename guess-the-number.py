import time
import os
import random
play = True
wrong = True

os.system('cls' if os.name=='nt' else 'clear')
print("----GUESS THE NUMBER----\n")
time.sleep(0.5)
print("Loading...")
time.sleep(0.5)
print("This may take a While...")
time.sleep(2)
print("Started correctly!")
time.sleep(0.3)
os.system('cls' if os.name=='nt' else 'clear')

while  play:
    numerorand = random.randint(1, 10)
    wrong = True
    while wrong:
        start = input("-x to Exit | Which is the number? (from 1-10)\n- ")
        
        if start == "x":
            play = False
            wrong = False

        elif int(start) == numerorand:
            print("You guessed it! Nice one!")
            time.sleep(1)
            wrong = False
            os.system('cls' if os.name=='nt' else 'clear')
            print("New Game!\n")
        
        else:
            if int(start) > numerorand:
                print("!!Try Again!! The number is LOWER than yours.")
                time.sleep(1.5)
                os.system('cls' if os.name=='nt' else 'clear')
            else:
                print("!!Try Again!! The number is HIGHER than yours.")
                time.sleep(1.5)
                os.system('cls' if os.name=='nt' else 'clear')

            wrong = True

print("\nThanks for playing! I hope you enjoyed it!\n")
input("Press /ENTER\ to Leave:\n")
os.system('cls' if os.name=='nt' else 'clear')