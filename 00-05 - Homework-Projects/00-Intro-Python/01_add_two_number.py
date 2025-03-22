def main():

    print("Welcome to Addition of 2 Numbers Program")
    
    num1: str = input("Enter the first number: ")
    num1: int = int(num1)
    
    num2: str = input("Enter the second number: ")
    num2: int = int(num2)
    
    total: int = num1 + num2
    
    print(f"Here is the sum of the two numbers: {total}")
    

if __name__ == '__main__':
    main()