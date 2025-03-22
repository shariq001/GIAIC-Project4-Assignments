import random

dice_sides: int = 5

def rolling_dice():
    
    dice1: int = random.randint(1, dice_sides)
    dice2: int = random.randint(1, dice_sides)
    
    total: int = dice1 + dice2
    print(f"Total of dices: {total}")
    
    
def main():
    
    dice: int = 10
    
    print(f"Dice in main() function is: {dice}")
    
    rolling_dice()
    rolling_dice()
    rolling_dice()
    
    print(f"Dice in main() function is: {dice}")
    
    print("\nThis ensures that the variables inside functions do not change global variables.")
    

if __name__ == "__main__":
    main()
    