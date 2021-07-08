import random
import time
import math

shell = [1, 2, 3, 4, 5, 6]

coin = ["head", "tail"]
coin_toss = random.choice(coin)
bullet = random.randint(1, 6)
print("WELCOME TO THE GAME OF DEATH")
time.sleep(5)
starting = "ONE BULLET IS LOADED INTO THE REVOLVER AND TRIGGER IS PULLED TURNWISE UNTIL PLAYER OR COMPUTER IS ELIMINATED"
print(starting)
time.sleep(5)
name = str(input("enter your name ")).upper()
i = str(input("head or tail?    ")).lower()
if i == coin_toss:
    c = [2, 4, 6]
    h = [1, 3, 5]
    time.sleep(5)
    print(f"{name}: My turn")
    for fire in shell:
        if fire % 2 == 0:

            if fire == bullet:
                time.sleep(5)
                print("COMPUTER : Pulled trigger")
                time.sleep(5)
                print("COMPUTER :YOU GOT SHOT...DIE...YOU LOSE!!!")
                print(f"the bullet was loaded in shell {bullet}")
                time.sleep(5)
                quit()
            else:
                time.sleep(5)
                print("COMPUTER : Pulled trigger")
                time.sleep(5)
                print("COMPUTER : fired blank")

        elif fire % 2 != 0:
            if fire == bullet:
                time.sleep(5)
                print(f"{name} : Pulled trigger")
                time.sleep(5)
                print(
                    "COMPUTER : It was loaded... NOOOOOOOO...I AM Dying..help me human...CONGRATS YOU  WINN!!!!")
                print(f"the bullet was loaded in shell {bullet}")
                time.sleep(5)
                quit()
            else:
                time.sleep(5)
                print(f"{name}: shot blank ....POFF")

else:
    h = [2, 4, 6]
    c = [1, 3, 5]
    time.sleep(5)
    print("COMPUTER : My turn")
    for fire in shell:
        if fire % 2 == 0:
            if fire == bullet:
                time.sleep(5)
                print(f"{name} : Pulled trigger")
                print(
                    "COMPUTER : AHHHHH...RIGHT IN THE HEART...HELP ME HUMAN...CONGRATS YOU WIN!!!!")
                print("THE BULLET WAS LOADED IN SHELL ", bullet)
                quit()
            else:
                time.sleep(5)
                print(f"{name} : shot blank ")

        elif fire % 2 != 0:
            if fire == bullet:
                time.sleep(5)
                print("COMPUTER :Pulled trigger")
                time.sleep(5)
                print("COMPUTER :  YOU GOT SHOT IN THE CHEST...DIE...YOU LOSE!!!")
                print("THE BULLET WAS LOADED IN SHELL ", bullet)
                quit()
            else:
                time.sleep(5)
                print("COMPUTER :Fired blank pofff")
