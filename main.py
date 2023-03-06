import random

def dice_roll(guess: bool = False):
    """
    Randomly give head or tail, if guess(param) True, you can choose your side
    """
    tup = ('head', 'tail')
    if guess:
        reply = str(input("Enter your side: (head, tail) "))

        if random.choice(tup) == reply:
            print("You win!")
        else:
            print("You lose")
    else:
        print(random.choice(tup))

if __name__ == "__main__":  
    dice_roll()
