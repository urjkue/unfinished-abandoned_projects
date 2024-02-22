
#idk why i did that :)

import random

simbols = {
    "joker": 30,
    "bells": 20,
    "cherry" :10
}

lucky_hand = []


def main():
    i = 1
    print("Hello")
    while(i<=3):
        random_name = random.choice(list(simbols.keys()))
        lucky_hand.append(random_name)
        i= i+1
    for x in lucky_hand:
        if(lucky_hand.index(x) == lucky_hand.index(x)+1 and lucky_hand.index(x) == lucky_hand.index(x)+2):
            print("You win")
            break
        else:
            print("You lose")
            print(lucky_hand)
            break

main()





