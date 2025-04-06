def main():
    
    print("\n- This Program converts feet to inches.")
    
    feet: float = float(input("\n- Enter the length in feet to convert to inches: "))
    
    inches: float = feet * 12
    
    print(f"\n {feet} feet is equal to {inches} inches.")


if __name__ == '__main__':
    main()
    