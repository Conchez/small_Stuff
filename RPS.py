# RPS Game with scoring system
import random
import time

comp_Score = 0
usr_Score = 0

item_List = ["a rock", "a piece of paper", "a pair of scissors"]
random_List = item_List.copy()
usr_Press = 1

print("We are going to play rock, paper, scissors!")
time.sleep(1.2)
usr_Name = input("To get started, enter your name!")

while usr_Press != "":
    usr_Press = input(f"Press ENTER to play {usr_Name}!")
    if usr_Press != "":
        print("YOU PRESS ENTER CHEESEHEAD... -_-")

        time.sleep(1.2)

    else:

        while usr_Press != "0":

            comp_Block = 0
            usr_Block = 0

            rock = 1
            paper = 2
            scissors = 3
            big_Rock = 4

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
                time.sleep(1)
                random.shuffle(random_List)
                comp_Choice = random_List[0]

                print(f"The computer's hand swiftly transforms into the shape of\n"
                      f"{comp_Choice}\n"
                      f"Your hand desperately tries to keep up and forms the shape of\n"
                      f"{true_Choice}!")

            if comp_Choice == "a pair of scissors":
                rock = big_Rock
            if true_Choice == "a pair of scissors":
                rock = big_Rock

            if comp_Choice == "a rock":
                comp_Block = rock
            if comp_Choice == "a piece of paper":
                comp_Block = paper
            if comp_Choice == "a pair of scissors":
                comp_Block = scissors

            if true_Choice == "a rock":
                usr_Block = rock
            if true_Choice == "a piece of paper":
                usr_Block = paper
            if true_Choice == "a pair of scissors":
                usr_Block = scissors

            if comp_Block > usr_Block:
                comp_Score = (comp_Score + 1)
            if usr_Block > comp_Block:
                usr_Score = (usr_Score + 1)
            if comp_Block == usr_Block:
                comp_Block = comp_Block
                usr_Block = usr_Block

            print(f"Computer: *{comp_Score}*     {usr_Name}: *{usr_Score}*")
