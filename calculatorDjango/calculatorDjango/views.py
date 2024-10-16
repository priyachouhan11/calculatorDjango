from django.shortcuts import render

def index(request):
   return render(request,'index.html')
# def index(request):
#   if request.method == 'POST':
#      action = request.POST.get('action')
#      display = request.POST.get('display','')

#      if action == 'AC':
#         display = ''
#      elif action == '=':
#         try:
#            display = str(eval(display))
#         except:
#            display = 'Error'
#      else:
#         display += action
#      return render(request,'index.html',{'display':display})               
#   return render(request,'index.html',{'display':''})

# def CubeRoot(num):
#     res = pow(num,1/3)
#     return res

class Calculator:

  def CubeRoot(num):
    res = pow(num,1/3)
    return res

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
