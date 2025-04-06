def main():
    
    c: int = 299792458 
    
    print("\nThis programs calculates the energy in Joules using the formula E = mc^2")
    print("\nwhere E is energy in Joules, m is mass in kilograms, and c is the speed of light in meters per second.")
    
    mass: float = float(input("\n- Enter the mass in kilograms: "))
    
    energy_in_joules: float = mass * c ** 2
    
    print("\ne = mc^2...")
    print(f"\nMass in Kilograms: {mass} kg")
    print(f"\nSpeed of Light {c} m/s")
    
    print(f"\nThe Energy in Joules is: {energy_in_joules} J")


if __name__ == '__main__':
    main()
    