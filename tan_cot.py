def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sin(x, terms=10):
    result = 0
    for n in range(terms):
        sign = 1 if (n % 2 == 0) else -1
        result += ((x ** (2 * n + 1)) / factorial(2 * n + 1)) * sign
    return abs(result)

def cos(x, terms=10):
    result = 0
    for n in range(terms):
        sign = 1 if (n % 2 == 0) else -1
        result += ((x ** (2 * n)) / factorial(2 * n)) * sign
    return abs(result)

def tan(angle_degrees, terms=10):
    angle_radians = (angle_degrees * 3.14159265358979323846) / 180
    sin_value = sin(angle_radians, terms)
    cos_value = cos(angle_radians, terms)
    if abs(cos_value) < 1e-10:
        raise ValueError("Cosine is too close to zero, tan is undefined")
    return abs(sin_value / cos_value)

def cot(angle_degrees, terms=10):
    angle_radians = (angle_degrees * 3.14159265358979323846) / 180
    sin_value = sin(angle_radians, terms)
    cos_value = cos(angle_radians, terms)
    if abs(sin_value) < 1e-10:
        raise ValueError("Sine is too close to zero, cot is undefined")
    return abs(cos_value / sin_value)

# Main program loop
while True:
    print("\nScientific Calculator - Trigonometric Functions")
    print("1. Calculate Sin")
    print("2. Calculate Cos")
    print("3. Calculate Tan")
    print("4. Calculate Cot")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    
    if choice in ['1', '2', '3', '4']:
        angle = float(input("Enter the angle in degrees: "))
        terms = int(input("Enter the number of terms for approximation (default is 10): ") or 10)
        
        try:
            angle_radians = (angle * 3.14159265358979323846) / 180
            if choice == '1':
                result = sin(angle_radians, terms)
                print(f"sin({angle}) ≈ {result}")
            elif choice == '2':
                result = cos(angle_radians, terms)
                print(f"cos({angle}) ≈ {result}")
            elif choice == '3':
                result = tan(angle, terms)
                print(f"tan({angle}) ≈ {result}")
            else:
                result = cot(angle, terms)
                print(f"cot({angle}) ≈ {result}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")