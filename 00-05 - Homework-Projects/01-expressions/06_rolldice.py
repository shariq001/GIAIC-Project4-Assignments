import random

dice_sides: int = 6

def main():
    print("This Program shows the random rolling of dices :)")
    
    dice1: int = random.randint(1, dice_sides);
    dice2: int = random.randint(1, dice_sides);
    
    total_of_dices: int = dice1 + dice2
    
    print(f"\n- The number of sides in each dice is: {dice_sides}")
    print(f"\n- The first dice: {dice1}")
    print(f"\n- The second dice: {dice2}")
    print(f"\n- The total of the dices is: {total_of_dices}")



if __name__ == '__main__':
    main()