# Helper function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Function to approximate sine using the Taylor series expansion 
def sine(x):
    sin_value = 0
    for n in range(10):  # Taylor series up to 10 terms
        term = ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)
        sin_value += term
    return sin_value

# Function to approximate cosine using the Taylor series expansion
def cosine(x):
    cos_value = 0
    for n in range(10):  # Taylor series up to 10 terms
        term = ((-1)**n * x**(2*n)) / factorial(2*n)
        cos_value += term
    return cos_value

# Function to calculate tangent (sin(x) / cos(x))
def tangent(x):
    return sine(x) / cosine(x)

# Function to calculate cotangent (1 / tangent(x))
def cotangent(x):
    return 1 / tangent(x)

# Function to calculate secant (1 / cos(x))
def secant(x):
    return 1 / cosine(x)

# Function to calculate cosecant (1 / sin(x))
def cosecant(x):
    return 1 / sine(x)

# Function to convert degrees to radians
def degrees_to_radians(degrees):
    pi = 22 / 7
    radians = (degrees * pi) / 180
    return radians

# Display Menu
def display_menu():
    print("\nScientific Calculator - Trigonometric Functions")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tan)")
    print("4. Cotangent (cot)")
    print("5. Secant (sec)")
    print("6. Cosecant (cosec)")
    print("7. Exit")

# Main Calculator Function
def scientific_calculator():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            degrees = float(input("Enter angle in degrees: "))
            radians = degrees_to_radians(degrees)

            if choice == '1':
                print(f"sin({degrees}°) = {sine(radians):.6f}")
            elif choice == '2':
                print(f"cos({degrees}°) = {cosine(radians):.6f}")
            elif choice == '3':
                print(f"tan({degrees}°) = {tangent(radians):.6f}")
            elif choice == '4':
                print(f"cot({degrees}°) = {cotangent(radians):.6f}")
            elif choice == '5':
                print(f"sec({degrees}°) = {secant(radians):.6f}")
            elif choice == '6':
                print(f"cosec({degrees}°) = {cosecant(radians):.6f}")
        
        elif choice == '7':
            print("Exiting calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid option.\n")

# Run the calculator
scientific_calculator()
