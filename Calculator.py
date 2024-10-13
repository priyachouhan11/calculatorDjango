def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def calculate_percentage(score, total):
            percentage = (score / total) * 100
            return percentage

def find_hcf(x,y):
    if (x < y):
        smaller=x
    else:
        smaller = y
    hcf=0
    for i in range(1,smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf = i
    return hcf

def log(base, value):
    result = 0
    while value > 1:
        value /= base
        result += 1
    return result

def power_of_x(x,y):
    n1 = x**y
    return n1

def square(s):
    sq = s**2
    return sq

def cube(c):
    cu = c**3
    return cu

def power_of_2(x):
    a = 2**x
    return a

def exponential(x, terms=10):
    result = 0
    for n in range(terms):
        result += (x ** n) / factorial(n)
    return result

def sine(x):
    sin_value = 0 
    for n in range(10):
        term = ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)
        sin_value += term
    return sin_value

def cosine(x):
    cos_value = 0
    for n in range(10):  
        term = ((-1)**n * x**(2*n)) / factorial(2*n)
        cos_value += term
    return cos_value

def tangent(x):
    return sine(x) / cosine(x)

def cotangent(x):
    return 1 / tangent(x)

def secant(x):
    return 1 / cosine(x)

def cosecant(x):
    return 1 / sine(x)

def degrees_to_radians(degrees):
    pi = 3.14159265359  
    degrees = degrees % 360
    if degrees < 0:
        degrees += 360
    radians = (degrees * pi) / 180
    return radians

def display_menu():
    print(" 1 for Factorial")
    print(" 2 for Percentage")
    print(" 3 for HCF")
    print(" 4 for log")
    print(" 5 for x**y")
    print(" 6 for x**2")
    print(" 7 for x**3")
    print(" 8 for 2**x")
    print(" 9 for e**x")
    print(" 10 for sine")
    print(" 11 for cosine")
    print(" 12 for tan")
    print(" 13 for cot")
    print(" 14 for sec")
    print(" 15 for cosec")
    

def scientific_calci():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if (choice==1):
            n = int(input("Enter the number: "))
            print(f"The factorial of te number is {factorial(n)}")
        elif (choice==2):
            score = int(input("Enter the score: "))
            total = int(input("Enter the total score: "))
            print(f"The percentage is: {calculate_percentage(score, total)}%.")
        elif (choice==3):
            num1=int(input("Enter first no:"))
            num2=int(input("Enter second no:"))
            print("The H.C.F. is ",find_hcf(num1,num2))
        elif (choice==4):
            base = int(input("Enter the base value: "))
            value = int(input("Enter the value: "))
            print(f"The logarithm of {value} with base {base} is {log(base, value)}")
        elif (choice==5):
            x = float(input("Enter the number here x:"))
            y = float(input("Enter the number here y:"))
            print(f"The x^y number is {power_of_x(x,y)}")
        elif (choice==6):
            s = eval(input("Enter the value: "))
            print(f"The square of {s} is {square(s)}")
        elif (choice==7):
            c = eval(input("Enter the value: "))
            print(f"The cube of {c} is {cube(c)}")
        elif (choice==8):
            x = eval(input("Enter the value of x: "))
            print(f"The value of the expressiion is {power_of_2(x)}")
        elif (choice==9):
            x = eval(input("Enter the x: "))
            print(f"The exponential value is {exponential(x)}")
        if (choice == 10,11,12,13,14,15):

            if (choice ==10):    
                degrees = eval(input("Enter angle in degrees: "))
                radians = degrees_to_radians(degrees)
                print(f"sin({degrees}°) = {sine(radians):.6f}")
            elif (choice==11):
                degrees = eval(input("Enter angle in degrees: "))
                radians = degrees_to_radians(degrees)
                print(f"cos({degrees}°) = {cosine(radians):.6f}")
            elif (choice==12):
                degrees = eval(input("Enter angle in degrees: "))
                radians = degrees_to_radians(degrees)
                print(f"tan({degrees}°) = {tangent(radians):.6f}")
            elif (choice==13):
                degrees = eval(input("Enter angle in degrees: "))
                radians = degrees_to_radians(degrees)
                print(f"cot({degrees}°) = {cotangent(radians):.6f}")
            elif (choice==14):
                degrees = eval(input("Enter angle in degrees: "))
                radians = degrees_to_radians(degrees)
                print(f"sec({degrees}°) = {secant(radians):.6f}")
            elif (choice==15):
                degrees = eval(input("Enter angle in degrees: "))
                radians = degrees_to_radians(degrees)
                print(f"cosec({degrees}°) = {cosecant(radians):.6f}")
        else:
            print("Invalid")
            break    

scientific_calci()