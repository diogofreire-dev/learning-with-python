def main():
    # Speed of light in meters per second (m/s)
    c = 300000000
    
    # Prompt the user for mass in kilograms
    mass = int(input("m: "))
    
    # Calculate energy using E = mc²
    energy = mass * (c ** 2)
    
    # Output the energy in Joules
    print(energy)

if __name__ == "__main__":
    main()