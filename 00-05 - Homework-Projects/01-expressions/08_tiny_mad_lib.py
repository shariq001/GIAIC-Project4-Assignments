def main():
    print("\nWelcome to the Mad Library Game!")
    
    adjective: str = input("\n- Enter an Adjective: ")
    noun: str = input("\n- Enter a Noun: ")
    verb: str = input("\n- Enter a Verb ")
    
    print(f"\n- The {adjective} {noun} jumped over the {noun} and tried to {verb} all day!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()