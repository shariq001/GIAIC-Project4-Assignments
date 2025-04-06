def main():
    
    print("\nThis Program helps in finding the quotient and remainder of dividing a number by another.")
    
    number1: int = int(input("\n- Enter the first number (dividend): "))
    
    number2: int = int(input("\n- Enter the second number (divisor): "))
    
    if number2 == 0:
        print("\n- Division by zero is not allowed.")
        return
    else:
        quotient: int = number1 // number2
        remainder: int = number1 % number2
        print(f"\n- The quotient of {number1} divided by {number2} is: {quotient} with a remainder of {remainder}.")
    
    


if __name__ == '__main__':
    main()
    