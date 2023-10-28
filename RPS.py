#RPS Game but WILD
import random
import time

item_List = ["a rock", "a piece of paper", "a pair of scissors"]
random_List = item_List.copy()
usr_Press = 1

print("We are going to play rock, paper, scissors!")

time.sleep(1.2)

while usr_Press != "":
    usr_Press = input("Press ENTER to play!")
    if usr_Press != "":
        print("YOU PRESS ENTER CHEESEHEAD... -_-")

        time.sleep(1.2)

    else:

        while usr_Press != "0":
            print("Alright, get ready!")
            player_Choice = input("Rock [1], Paper [2], Scissors [3], Quit [0]")
            if player_Choice == "0":
                exit()
            else:
                true_Choice = item_List[int(player_Choice) - 1]
                time.sleep(0.9)
                print("ROCK!")
                time.sleep(0.9)
                print("PAPER!")
                time.sleep(0.9)
                print("SCISSORS!")
                time.sleep(0.9)
                print("SHOOT!")
                time.sleep(1.5)
                random.shuffle(random_List)
                comp_Choice = random_List[0]

                print(f"The computer's hand swiftly transforms into the shape of\n"
                      f"{comp_Choice}\n"
                      f"Your hand desperately tries to keep up and forms the shape of\n"
                      f"{true_Choice}!")

