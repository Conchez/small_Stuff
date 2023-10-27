#This will give you a random place to eat!
import random
rest_List = []
Rest = 1
while Rest != "ok":
    Rest = input('Where would you like to go?\n'
                 'When you are finished, type "ok" and hit enter!')

    if Rest != "ok":
        rest_List.append(Rest)

    else:
        random.shuffle(rest_List)
        print(f"If it were me, I'd go to {rest_List[0]}.")

