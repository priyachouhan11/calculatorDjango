a = int(input('Enter the value of a'))
b=  int(input('Enter the value of b'))
c = int(input('Enter the value of c'))

discriminant = b**2 - 4*a*c
if discriminant > 0:
        # Two distinct real roots
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print(root1, root2)
elif discriminant == 0:
        # One real root (repeated)
     root = -b / (2*a)
     print(root)
else:
    # Complex roots
     real_part = -b / (2*a)
     imaginary_part = (abs(discriminant)**0.5) / (2*a)
     root1 = complex(real_part, imaginary_part)
     root2 = complex(real_part, -imaginary_part)
     print(root1, root2)

