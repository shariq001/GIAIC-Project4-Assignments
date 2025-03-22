def main():
    print("Welcome to Fahreinheit to Celcius Templerature Program!")
    
    fahreinheit: str = input("Enter the temperature in Fahreinheit: ")
    fahreinheit: float = float(fahreinheit)
    
    celcius: float = (fahreinheit - 32) * 5.0/9.0
    
    print(f"The temperature in Celciu is: {celcius}")


if __name__ == '__main__':
    main()