# This is a magic Mentalo emulator!
# Program allows the user to ask a question, and "Mentalo" gives a random response from his list of responses!
import random
import time

ask_mentalo = ["What other secrets do you want to know?",
               "What other forbidden knowledge can I help you see?",
               "The universe wants to give you the answers. What else would you like to ask?",
               "I sense you have more to ask. What can I answer for you friend?"]

all_mentalo_Resp = ["The spirits around you seem unsure.",
                    "The universe is not sure what to think. Your inquiry remains a mystery.",
                    "The cosmic jury is still out, my friend. I'm uncertain.",
                    "I'm afraid the answer remains a secret my friend.",
                    "The reaper has informed me it is a definite no!",
                    "I'm sensing the word no looming throughout the realm unseen.",
                    "I'm seeing an abhorrent curse come upon you, absolutely no!",
                    'The spirits from beyond the grave say no!',
                    'My sources from beyond the grave say yes!',
                    "My crystal ball reveals a resounding yes!",
                    "The universe nods in your favor, it is certain.",
                    "The spirits around me are whispering yes!"]

random.shuffle(all_mentalo_Resp)
random.shuffle(ask_mentalo)

usr_Question = "1"

print("Hello friend.")
time.sleep(1.25)
print("I am Mentalo, the great Seer.")
usr_Name = input("What should I call you?")
time.sleep(0.3)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(f"Ah yes. I'm sensing. I should have known it was you {usr_Name}.\n"
      f"")

if usr_Name.lower() == "lauren":
    time.sleep(1.5)
    print("I see you are very special.\n"
          "")
    time.sleep(1.5)
    print("I sense a very strong connection between you and my creator, Connor.\n"
          "")
    time.sleep(1.5)
    print("The universe tells me true love and a happy future together are certain.\n"
          "")

time.sleep(2.1)

if usr_Question != "0":
    usr_Question = input("If you feel like an answer is not destined to be known, press 0 to un-summon me.\n"
                         "Now that I've gotten that out of the way for liability purposes, \n"
                         "What would you like to know friend?")


    if usr_Question == "0":
        print("")
        print("I see the cosmic answers are becoming overwhelming for you.")
        time.sleep(2.5)
        print(f"The spirits tell me we will meet again soon {usr_Name}.")
        time.sleep(2)
        exit()

    if usr_Question != "0":
        time.sleep(0.3)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(all_mentalo_Resp[0])

    time.sleep(1.5)

while usr_Question != "0":
    random.shuffle(all_mentalo_Resp)
    random.shuffle(ask_mentalo)

    usr_Question = input(ask_mentalo[0])

    if usr_Question == "0":
        print("")
        print("I see the cosmic answers are becoming overwhelming for you.")
        time.sleep(2.5)
        print(f"The spirits tell me we will meet again soon {usr_Name}.")
        time.sleep(2)
        exit()

    time.sleep(0.3)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)

    print(all_mentalo_Resp[0])

    time.sleep(1.5)
