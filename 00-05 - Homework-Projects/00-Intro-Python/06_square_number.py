def main():
    print("Welcome to Square Number Program!")
    
    number: str = input("Enter the number you want to square: ")
    number: float = float(number)
    
    square: float = number ** 2
    
    print(f"The square of the number {number} is: {square}")


if __name__ == '__main__':
    main()