def main():
    print("Welcome to Triangle Perimeter Program!")
    
    side1: str = input("Enter the length of side 1 of trinagle: ")
    side1: float = float(side1)
    
    side2: str = input("Enter the length of side 2 of trinagle: ")
    side2: float = float(side2)
    
    side3: str = input("Enter the length of side 3 of trinagle: ")
    side3: float = float(side3)
    
    perimeter: float = side1 + side2 + side3
    
    print(f"The perimeter of the triangle is: {perimeter}")
    
    


if __name__ == '__main__':
    main()