import math

def main():
    
    print("\nThis Program helps in finding the length of the hypotenuse of a right triangle.")
    
    print("\n Let Triangle ABC be a right triangle with right angle at B.")
    
    AB: float = float(input("\n- Enter the length of side AB (the perpendicular side):"))
    
    BC: float = float(input("\n- Enter the length of side BC (the base side):"))
    
    AC: float = math.sqrt(AB ** 2 + BC ** 2)
    
    print(f"\nThe length of the hypotenuse AC is: {AC}")


if __name__ == '__main__':
    main()
    